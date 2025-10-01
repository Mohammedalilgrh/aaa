import os
import sys
import time
import json
import threading
import subprocess
from queue import Queue, Empty
from pathlib import Path

# --- Auto-install helper (best-effort) ---
REQS = [
    "selenium>=4.0.0",
    "pyautogui",
    "pillow",
    "pytesseract",
    "opencv-python",
    "numpy",
    "requests",
    "python-dotenv",
    "pyttsx3",
    "pygetwindow",
]

# optional voice libs (may fail to pip install on Windows without wheels)
OPTIONAL = ["SpeechRecognition", "pyaudio"]

def pip_install(packages):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])
    except Exception as e:
        print("Warning: pip install failed for", packages, "->", e)

# Try install packages silently (won't break if already installed)
try:
    import importlib
    for pkg in REQS:
        module_name = pkg.split("==")[0].split(">")[0].split("<")[0]
        if importlib.util.find_spec(module_name) is None:
            print(f"Installing {pkg} ...")
            pip_install([pkg])
    for pkg in OPTIONAL:
        if importlib.util.find_spec(pkg) is None:
            print(f"Installing optional {pkg} ...")
            pip_install([pkg])
except Exception as e:
    print("Auto-install step had issues:", e)

# Now import modules (after attempted install)
import requests
import pytesseract
import cv2
import numpy as np
from PIL import Image
import pyautogui
import pygetwindow as gw
import pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

# Try optional imports
try:
    import speech_recognition as sr
except Exception:
    sr = None

# --- Configuration ---
BASE_DIR = Path.cwd()
ENV_PATH = BASE_DIR / ".env"
if not ENV_PATH.exists():
    # allow reading from system env too
    pass
load_dotenv(dotenv_path=str(ENV_PATH))

ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY") or ""
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH") or str(BASE_DIR / "chromedriver-win64" / "chromedriver.exe")
TESSERACT_CMD = os.getenv("TESSERACT_CMD") or None
if TESSERACT_CMD:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

MEMORY_FILE = BASE_DIR / "memory.json"
NOTES_FILE = BASE_DIR / "agent_notes.txt"
SCREENSHOT_DIR = BASE_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

ANTHROPIC_MESSAGES_URL = "https://api.anthropic.com/v1/messages"

# --- Utilities ---
def save_memory(item):
    mem = []
    if MEMORY_FILE.exists():
        try:
            mem = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            mem = []
    mem.append({"ts": time.time(), "item": item})
    MEMORY_FILE.write_text(json.dumps(mem, ensure_ascii=False, indent=2), encoding="utf-8")

def append_note(text):
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()}: {text}\n\n")

# --- Anthropic simple wrapper (Messages API) ---
def anthropic_message(system="", user=""):
    if not ANTHROPIC_KEY:
        raise Exception("ANTHROPIC_API_KEY not set (put in .env or env vars)")
    headers = {
        "x-api-key": ANTHROPIC_KEY,
        "Content-Type": "application/json",
    }
    body = {"model":"claude-3.5-sonnet-20241022","messages":[{"role":"system","content":system},{"role":"user","content":user}]}
    try:
        r = requests.post(ANTHROPIC_MESSAGES_URL, headers=headers, json=body, timeout=120)
        r.raise_for_status()
        j = r.json()
        # Many providers return messages in different shapes; try to extract text:
        if "token" in j:
            # unknown shape
            return str(j)
        # Typical shape: {'id':..., 'model':..., 'messages':[{'role':'assistant','content':...}], ...}
        if "messages" in j and isinstance(j["messages"], list):
            for m in reversed(j["messages"]):
                if m.get("role") in ("assistant","model","system") and m.get("content"):
                    return m.get("content")
        # Some docs show "completion" or "output":
        if "completion" in j:
            return j["completion"]
        if "output" in j:
            return j["output"]
        return json.dumps(j)
    except Exception as e:
        return f"[anthropic error] {e} - raw response: {getattr(e,'response',None)}"

# --- Screen analysis + OCR thread ---
SCREEN_QUEUE = Queue()

def screen_analyzer_loop(interval=2.0):
    print("[ScreenAnalyzer] started (press Ctrl+C to stop)")
    last_text = ""
    idx = 0
    while True:
        try:
            img = pyautogui.screenshot()
            fname = SCREENSHOT_DIR / f"screen_{int(time.time())}_{idx}.png"
            img.save(str(fname))
            idx += 1
            # OCR
            pil = Image.open(str(fname)).convert("L")
            arr = np.array(pil)
            text = ""
            try:
                text = pytesseract.image_to_string(arr)
            except Exception as e:
                text = ""
            # simple diff detect
            if len(text.strip())>20 and text.strip() != last_text:
                last_text = text.strip()
                print("[ScreenAnalyzer] detected text (snippet):", (text.strip()[:200]).replace("\n"," "))
                append_note("OCR snippet:\n"+text.strip()[:1000])
                save_memory({"type":"ocr","text":text.strip()[:1000],"img":str(fname)})
        except Exception as e:
            print("[ScreenAnalyzer] error:", e)
        time.sleep(interval)

# --- Selenium browser automation helpers ---
class BrowserController:
    def __init__(self, chromedriver_path=None, headless=False):
        self.driver = None
        self.chromedriver_path = chromedriver_path or CHROMEDRIVER_PATH
        self.headless = headless
        self.lock = threading.Lock()

    def start(self):
        with self.lock:
            if self.driver is not None:
                return
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            try:
                service = ChromeService(executable_path=self.chromedriver_path)
                self.driver = webdriver.Chrome(service=service, options=options)
                print("[Browser] Chrome started")
            except Exception as e:
                print("[Browser] Failed to start Chrome via chromedriver:", e)
                self.driver = None

    def open_url(self, url):
        self.start()
        if not self.driver:
            print("[Browser] driver not available")
            return False
        try:
            self.driver.get(url)
            time.sleep(1.0)
            return True
        except Exception as e:
            print("[Browser] open_url error:", e)
            return False

    def search_google(self, query, top_n=5):
        ok = self.open_url("https://www.google.com")
        if not ok: return []
        try:
            time.sleep(1.2)
            q = self.driver.find_element(By.NAME, "q")
            q.send_keys(query)
            q.send_keys(Keys.ENTER)
            time.sleep(1.2)
            links = self.driver.find_elements(By.CSS_SELECTOR, "a")
            results = []
            for a in links:
                href = a.get_attribute("href")
                text = a.text
                if href and href.startswith("http") and text:
                    results.append({"text": text.strip(), "href": href})
                if len(results) >= top_n:
                    break
            return results
        except Exception as e:
            print("[Browser] search_google error:", e)
            return []

    def click_link_by_text(self, text):
        if not self.driver: return False
        try:
            elems = self.driver.find_elements(By.PARTIAL_LINK_TEXT, text)
            if elems:
                elems[0].click()
                time.sleep(1.0)
                return True
            return False
        except Exception as e:
            print("[Browser] click_link_by_text error:", e)
            return False

    def get_page_text(self):
        if not self.driver: return ""
        try:
            return self.driver.execute_script("return document.body.innerText")
        except Exception as e:
            return ""

    def screenshot(self, name=None):
        name = name or f"page_{int(time.time())}.png"
        path = SCREENSHOT_DIR / name
        if self.driver:
            try:
                self.driver.save_screenshot(str(path))
                return str(path)
            except Exception as e:
                print("[Browser] screenshot error:", e)
        else:
            # fallback to full screen capture
            img = pyautogui.screenshot()
            img.save(str(path))
            return str(path)
        return None

# --- Action execution (interpret JSON from AI) ---
def execute_action_sequence(actions, browser: BrowserController):
    """
    actions: list of dicts, each dict: {"action":"open_url" / "search" / "click" / "type" / "save_note", "value":...}
    """
    results = []
    for a in actions:
        try:
            act = a.get("action")
            val = a.get("value")
            print("[Executor] action:", act, val)
            if act == "open_url":
                ok = browser.open_url(val)
                results.append({"action":act,"ok":ok})
            elif act == "search":
                res = browser.search_google(val, top_n = int(a.get("top_n",5)))
                results.append({"action":act,"results":res})
            elif act == "click_link_by_text":
                ok = browser.click_link_by_text(val)
                results.append({"action":act,"ok":ok})
            elif act == "get_page_text":
                txt = browser.get_page_text()
                results.append({"action":act,"text_sample":txt[:1000]})
                append_note("Page text sample:\n"+txt[:2000])
            elif act == "screenshot":
                p = browser.screenshot(val if isinstance(val,str) else None)
                results.append({"action":act,"path":p})
            elif act == "save_note":
                append_note(val)
                results.append({"action":act,"ok":True})
            elif act == "type":
                # type into active element using pyautogui as fallback
                pyautogui.typewrite(str(val), interval=0.02)
                results.append({"action":act,"ok":True})
            elif act == "press":
                pyautogui.press(val)
                results.append({"action":act,"ok":True})
            elif act == "wait":
                time.sleep(float(val))
                results.append({"action":act,"ok":True})
            else:
                # unknown action => store as note and continue
                append_note(f"Unknown action requested by AI: {a}")
                results.append({"action":act,"ok":False,"reason":"unknown"})
        except Exception as e:
            results.append({"action":a,"ok":False,"error":str(e)})
    return results

# --- Conversation loop / interpreter ---
def build_system_prompt():
    return (
        "You are an assistant that outputs actions for a desktop automation agent. "
        "When asked to perform tasks, respond with JSON ONLY when you want the agent to execute steps. "
        "JSON format: {\"actions\":[ {\"action\":\"open_url\",\"value\":\"https://...\"}, "
        "{\"action\":\"search\",\"value\":\"search terms\",\"top_n\":5}, "
        "{\"action\":\"click_link_by_text\",\"value\":\"...\"}, "
        "{\"action\":\"get_page_text\"}, {\"action\":\"screenshot\",\"value\":\"optional_name.png\"}, "
        "{\"action\":\"save_note\",\"value\":\"some text to save\"} ] }\n\n"
        "If you only want to reply with text or give advice, return plain text (not JSON). "
        "If a CAPTCHA appears say exactly: NEEDS_MANUAL_CAPTCHA and wait for the user to solve it and confirm."
    )

def parse_and_execute_ai_response(ai_text, browser: BrowserController):
    # Try parse JSON
    ai_text_stripped = ai_text.strip()
    try:
        # find first JSON object inside text
        start = ai_text_stripped.find("{")
        end = ai_text_stripped.rfind("}")
        if start != -1 and end != -1 and end>start:
            j = json.loads(ai_text_stripped[start:end+1])
            actions = j.get("actions", [])
            res = execute_action_sequence(actions, browser)
            save_memory({"type":"executed_actions","actions":actions,"result":res})
            return {"executed":True,"result":res}
    except Exception as e:
        print("[Parser] JSON parse failed:", e)
    # else treat as plain text
    save_memory({"type":"ai_text","text":ai_text_stripped})
    return {"executed":False,"text":ai_text_stripped}

# --- TTS ---
tts_engine = None
def speak_text(text):
    global tts_engine
    try:
        if tts_engine is None:
            tts_engine = pyttsx3.init()
            tts_engine.setProperty('rate', 170)
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print("[TTS] error:", e)

# --- Main interactive loop ---
def interactive_loop():
    print("=== Smart Desktop Agent ===")
    print("Type your message and press Enter. Type /voice to toggle voice input (if available). Type /exit to quit.")
    browser = BrowserController()
    # start screen analyzer thread
    t = threading.Thread(target=screen_analyzer_loop, args=(2.0,), daemon=True)
    t.start()
    browser.start()
    voice_enabled = True if sr is not None else False
    while True:
        try:
            user_input = input("\nYou: ")
            if not user_input:
                # if empty line, try voice if available
                if voice_enabled:
                    print("[Voice] Listening... (say something)")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.listen(source, timeout=8, phrase_time_limit=12)
                    try:
                        text = r.recognize_google(audio)
                        print("You (voice):", text)
                        user_input = text
                    except Exception as e:
                        print("Voice recognition failed:", e)
                        continue
                else:
                    continue

            if user_input.lower().strip() in ("/exit","exit","quit"):
                print("Exiting...")
                break
            if user_input.lower().strip() == "/voice":
                voice_enabled = not voice_enabled
                print("Voice enabled:", voice_enabled)
                continue

            # Prepare system prompt + user message
            system = build_system_prompt()
            ai_response = anthropic_message(system=system, user=user_input)
            print("\n[AI raw response]:\n", ai_response)
            # If AI asked for manual captcha
            if "NEEDS_MANUAL_CAPTCHA" in ai_response:
                print("AI indicates a CAPTCHA must be solved manually. Please solve it in the browser, then press Enter to continue.")
                input("Press Enter after completing CAPTCHA...")
                save_memory({"type":"captcha_solved","by_user":True})
                # Optionally inform AI to continue
                ai_response = anthropic_message(system=system, user="CAPTCHA solved, continue.")
                print("[AI continuation]:", ai_response)

            parsed = parse_and_execute_ai_response(ai_response, browser)
            if parsed.get("executed"):
                print("[Executed actions result]:", json.dumps(parsed["result"], indent=2, ensure_ascii=False))
            else:
                # plain text reply: speak and save
                print("\nAI:", parsed.get("text"))
                append_note("AI reply:\n"+(parsed.get("text") or "")[:2000])
                # speak
                threading.Thread(target=speak_text, args=(parsed.get("text") or "",), daemon=True).start()

        except KeyboardInterrupt:
            print("Interrupted by user. Exiting.")
            break
        except Exception as e:
            print("Error in interactive loop:", e)

# --- Start point ---
if __name__ == "__main__":
    print("Agent starting... (CWD:", BASE_DIR, ")")
    print("Make sure .env has ANTHROPIC_API_KEY and CHROMEDRIVER_PATH set.")
    # quick checks:
    if not ANTHROPIC_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set. Put it in .env or env vars.")
        sys.exit(1)
    if not Path(CHROMEDRIVER_PATH).exists():
        print(f"WARNING: chromedriver not found at {CHROMEDRIVER_PATH}. Please put chromedriver.exe there, or edit .env CHROMEDRIVER_PATH.")
        # attempt to continue; Browser start will fail if not fixed
    # start interactive loop
    interactive_loop()
