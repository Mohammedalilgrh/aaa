import os
import sys
import subprocess
import time
import json
import threading
import pyautogui
import requests
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageGrab
import keyboard
import pyperclip
import pandas as pd
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import google.generativeai as genai
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random
import re
import webbrowser
import socket
import psutil
import win32api
import win32con
import win32gui
import win32process
import win32clipboard
import pygetwindow as gw
import mss
import mss.tools
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
import asyncio
import aiohttp
import asyncio
import aiofiles
import hashlib
import base64
import secrets
import uuid
import logging
import queue
import signal
import atexit
import tempfile
import zipfile
import tarfile
import shutil
import glob
import fnmatch
import stat
import ctypes
import ctypes.wintypes
import winreg
import wmi
import pywinauto
from pywinauto import Application
from pywinauto.findwindows import find_elements
import pyautogui._pyautogui_win as winInfo
import pygetwindow as gw
import pyautogui._pyautogui_win as winInfo
import pygetwindow as gw
import pyautogui._pyautogui_win as winInfo

# Initialize colorama
init()

# === ULTIMATE HUMANITY AI AGENT WITH FULL TEAMVIEWER-LIKE CONTROL ===
GEMINI_KEY = "AIzaSyDnsQ_EaKER5TghXoh8mpkoy_tXZoaYZ58"
QWEN_KEY = "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"
GPT4_KEY = "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"

# Configure all APIs
genai.configure(api_key=GEMINI_KEY)
qwen_client = OpenAI(api_key=QWEN_KEY, base_url="https://openrouter.ai/api/v1")
gpt4_client = OpenAI(api_key=GPT4_KEY)

# Setup data directories
DATA_DIR = "ultimate_humanity_agent_data"
os.makedirs(DATA_DIR, exist_ok=True)
SCREENSHOTS_DIR = os.path.join(DATA_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
DOWNLOADS_DIR = os.path.join(DATA_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
LOGS_DIR = os.path.join(DATA_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
TEMP_DIR = os.path.join(DATA_DIR, "temp")
os.makedirs(TEMP_DIR, exist_ok=True)

HISTORY_FILE = os.path.join(DATA_DIR, "history.json")
LOG_FILE = os.path.join(DATA_DIR, "agent.log")

# Setup logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def log(msg, color=Fore.WHITE):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    colored_msg = f"{color}[{timestamp}] {msg}{Style.RESET_ALL}"
    print(colored_msg)
    logger.info(msg)

# Load conversation history
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

# Save conversation history
def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# Initialize advanced browser
def init_advanced_browser():
    try:
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-extensions")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--enable-features=NetworkService")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Remove webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        log("[✓] ULTIMATE BROWSER STARTED (TeamViewer-like)", Fore.GREEN)
        return driver
    except Exception as e:
        log(f"[ERROR] Failed to start advanced browser: {e}", Fore.RED)
        return None

# Global state
driver = None
history = load_history()
running = True
current_window = None
current_process = None

# === ADVANCED CORE FUNCTIONS (1000+ lines) ===

def execute_cmd(command):
    log(f"[CMD] Executing: {command}", Fore.CYAN)
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout or result.stderr
        log(f"[CMD OUTPUT]\n{output[:500]}", Fore.YELLOW)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[CMD TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[CMD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def open_new_note():
    try:
        subprocess.run(["notepad.exe"], shell=True)
        time.sleep(1)
        log("[✓] New note opened (Notepad)", Fore.GREEN)
        return "[✓] New note opened (Notepad)"
    except Exception as e:
        try:
            temp_file = os.path.join(DATA_DIR, "new_note.txt")
            with open(temp_file, "w") as f:
                f.write("# New Note\n\n")
            os.startfile(temp_file)
            time.sleep(1)
            log(f"[✓] New note opened: {temp_file}", Fore.GREEN)
            return f"[✓] New note opened: {temp_file}"
        except Exception as e2:
            err = f"[NOTE ERROR] {str(e2)}"
            log(err, Fore.RED)
            return err

def write_to_note(content):
    try:
        time.sleep(1)
        pyautogui.write(content, interval=0.01)
        log(f"[WRITE] Content written to note ({len(content)} chars)", Fore.CYAN)
        return f"[✓] Content written to note ({len(content)} chars)"
    except Exception as e:
        err = f"[WRITE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def save_note():
    try:
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+s')
        time.sleep(1)
        keyboard.press_and_release('enter')
        log("[SAVE] Note saved successfully", Fore.CYAN)
        return "[✓] Note saved successfully"
    except Exception as e:
        err = f"[SAVE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        log(f"[COPY] Text copied to clipboard ({len(text)} chars)", Fore.CYAN)
        return f"[✓] Text copied to clipboard ({len(text)} chars)"
    except Exception as e:
        err = f"[COPY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def paste_from_clipboard():
    try:
        text = pyperclip.paste()
        log(f"[PASTE] Text pasted from clipboard ({len(text)} chars)", Fore.CYAN)
        return text
    except Exception as e:
        err = f"[PASTE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        log(f"[READ] {path} ({len(content)} chars)", Fore.CYAN)
        return content[:2000]
    except Exception as e:
        err = f"[READ ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def write_file(path, content):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"[WRITE] {path} ({len(content)} chars)", Fore.CYAN)
        return f"[✓] Written to {path}"
    except Exception as e:
        err = f"[WRITE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        filepath = os.path.join(SCREENSHOTS_DIR, filename)
        screenshot.save(filepath)
        log(f"[SCREENSHOT] Saved: {filepath}", Fore.CYAN)
        return f"[✓] Screenshot saved: {filepath}"
    except Exception as e:
        err = f"[SCREENSHOT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def move_mouse(x, y, action="move"):
    log(f"[MOUSE] {action} to ({x}, {y})", Fore.CYAN)
    pyautogui.moveTo(x, y, duration=0.1)
    if action == "click":
        pyautogui.click()
    elif action == "double_click":
        pyautogui.doubleClick()
    elif action == "right_click":
        pyautogui.rightClick()
    elif action == "middle_click":
        pyautogui.middleClick()
    return f"[MOUSE] {action} at ({x}, {y})"

def scroll_mouse(clicks):
    try:
        pyautogui.scroll(clicks)
        log(f"[SCROLL] Scrolled {clicks} clicks", Fore.CYAN)
        return f"[✓] Scrolled {clicks} clicks"
    except Exception as e:
        err = f"[SCROLL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def drag_mouse(x1, y1, x2, y2, duration=0.5):
    try:
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, duration=duration)
        log(f"[DRAG] Dragged from ({x1}, {y1}) to ({x2}, {y2})", Fore.CYAN)
        return f"[✓] Dragged from ({x1}, {y1}) to ({x2}, {y2})"
    except Exception as e:
        err = f"[DRAG ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def type_text(text):
    log(f"[TYPE] {text[:50]}...", Fore.CYAN)
    pyautogui.write(text, interval=0.01)
    return f"[TYPED] {text[:30]}..."

def press_key(key):
    try:
        pyautogui.press(key)
        log(f"[KEY] Pressed key: {key}", Fore.CYAN)
        return f"[✓] Pressed key: {key}"
    except Exception as e:
        err = f"[KEY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def press_hotkey(*keys):
    try:
        pyautogui.hotkey(*keys)
        log(f"[HOTKEY] Pressed: {'+'.join(keys)}", Fore.CYAN)
        return f"[✓] Pressed: {'+'.join(keys)}"
    except Exception as e:
        err = f"[HOTKEY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def find_window(title):
    try:
        windows = gw.getWindowsWithTitle(title)
        if windows:
            window = windows[0]
            log(f"[WINDOW] Found window: {title}", Fore.CYAN)
            return window
        else:
            log(f"[WINDOW] Window not found: {title}", Fore.RED)
            return None
    except Exception as e:
        err = f"[WINDOW ERROR] {str(e)}"
        log(err, Fore.RED)
        return None

def focus_window(title):
    try:
        window = find_window(title)
        if window:
            window.activate()
            log(f"[WINDOW] Focused window: {title}", Fore.CYAN)
            return f"[✓] Focused window: {title}"
        else:
            return f"[WINDOW] Window not found: {title}"
    except Exception as e:
        err = f"[FOCUS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def minimize_window(title):
    try:
        window = find_window(title)
        if window:
            window.minimize()
            log(f"[WINDOW] Minimized: {title}", Fore.CYAN)
            return f"[✓] Minimized: {title}"
        else:
            return f"[WINDOW] Window not found: {title}"
    except Exception as e:
        err = f"[MINIMIZE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def maximize_window(title):
    try:
        window = find_window(title)
        if window:
            window.maximize()
            log(f"[WINDOW] Maximized: {title}", Fore.CYAN)
            return f"[✓] Maximized: {title}"
        else:
            return f"[WINDOW] Window not found: {title}"
    except Exception as e:
        err = f"[MAXIMIZE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def close_window(title):
    try:
        window = find_window(title)
        if window:
            window.close()
            log(f"[WINDOW] Closed: {title}", Fore.CYAN)
            return f"[✓] Closed: {title}"
        else:
            return f"[WINDOW] Window not found: {title}"
    except Exception as e:
        err = f"[CLOSE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def search_google(query):
    global driver
    if not driver:
        driver = init_advanced_browser()
        if not driver:
            import webbrowser
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            log(f"[BROWSER] Opening search in default browser: {url}", Fore.CYAN)
            return "[✓] Search opened in default browser"
    
    log(f"[BROWSER] Searching Google for: {query}", Fore.CYAN)
    try:
        driver.get(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        time.sleep(1)
        
        try:
            results = driver.find_elements(By.CSS_SELECTOR, "h3")
            top_results = [result.text for result in results[:5] if result.text]
            
            if top_results:
                log(f"[SEARCH RESULTS]", Fore.GREEN)
                for i, result in enumerate(top_results, 1):
                    log(f"  {i}. {result}", Fore.YELLOW)
        except:
            pass
        
        return f"[✓] Google search completed. Found {len(top_results) if 'top_results' in locals() else 0} results"
    except Exception as e:
        err = f"[BROWSER ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def browse_url(url):
    global driver
    if not driver:
        driver = init_advanced_browser()
        if not driver:
            import webbrowser
            webbrowser.open(url.strip())
            log(f"[BROWSER] Opening in default browser: {url.strip()}", Fore.CYAN)
            return "[✓] URL opened in default browser"
    
    log(f"[BROWSER] Opening: {url}", Fore.CYAN)
    url = url.strip()
    try:
        driver.get(url)
        time.sleep(1)
        return "[✓] Page loaded"
    except Exception as e:
        err = f"[BROWSER ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def extract_page_content():
    global driver
    if not driver:
        return "[ERROR] No browser open"
    try:
        page_content = driver.find_element(By.TAG_NAME, "body").text
        log(f"[PAGE CONTENT] Extracted {len(page_content)} chars", Fore.CYAN)
        return page_content[:3000]
    except Exception as e:
        err = f"[EXTRACT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def click_element(selector, selector_type="css"):
    global driver
    if not driver:
        return "[ERROR] No browser open"
    try:
        if selector_type == "css":
            element = driver.find_element(By.CSS_SELECTOR, selector)
        elif selector_type == "xpath":
            element = driver.find_element(By.XPATH, selector)
        elif selector_type == "id":
            element = driver.find_element(By.ID, selector)
        elif selector_type == "name":
            element = driver.find_element(By.NAME, selector)
        else:
            return "[ERROR] Invalid selector type"
        
        element.click()
        log(f"[CLICK] Clicked element: {selector}", Fore.CYAN)
        return f"[✓] Clicked element: {selector}"
    except Exception as e:
        err = f"[CLICK ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def fill_form_field(selector, value, selector_type="css"):
    global driver
    if not driver:
        return "[ERROR] No browser open"
    try:
        if selector_type == "css":
            element = driver.find_element(By.CSS_SELECTOR, selector)
        elif selector_type == "xpath":
            element = driver.find_element(By.XPATH, selector)
        elif selector_type == "id":
            element = driver.find_element(By.ID, selector)
        elif selector_type == "name":
            element = driver.find_element(By.NAME, selector)
        else:
            return "[ERROR] Invalid selector type"
        
        element.clear()
        element.send_keys(value)
        log(f"[FORM] Filled field {selector} with: {value[:20]}...", Fore.CYAN)
        return f"[✓] Filled field {selector} with: {value[:20]}..."
    except Exception as e:
        err = f"[FORM ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def check_for_login_or_captcha():
    global driver
    if not driver:
        return False
    try:
        page_text = driver.find_element(By.TAG_NAME, "body").text.lower()
        if any(kw in page_text for kw in ["sign in", "login", "captcha", "verify", "robot", "consent", "verify you are human", "sign up", "register"]):
            log("\n[⚠️  ACTION REQUIRED] Detected login, CAPTCHA, or signup page!", Fore.RED)
            log("Please handle this manually in the browser window.", Fore.RED)
            input("Press ENTER in this CMD window when you're done...")
            return True
    except:
        pass
    return False

def download_file(url, filename):
    try:
        response = requests.get(url)
        filepath = os.path.join(DOWNLOADS_DIR, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        log(f"[DOWNLOAD] File saved: {filepath}", Fore.CYAN)
        return f"[✓] Downloaded: {filepath}"
    except Exception as e:
        err = f"[DOWNLOAD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def scrape_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        links = soup.find_all('a', href=True)
        
        content = {
            'title': soup.title.string if soup.title else 'No title',
            'paragraphs': [p.get_text().strip() for p in paragraphs[:10]],
            'links': [link['href'] for link in links[:20]]
        }
        
        log(f"[SCRAPE] Extracted content from {url}", Fore.CYAN)
        return str(content)
    except Exception as e:
        err = f"[SCRAPE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def find_and_open_multiple_pages(query, num_pages=5):
    global driver
    if not driver:
        driver = init_advanced_browser()
        if not driver:
            return "[ERROR] No browser available"
    
    try:
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        driver.get(search_url)
        time.sleep(2)
        
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        opened_pages = []
        
        for i, result in enumerate(results[:num_pages]):
            try:
                result.click()
                time.sleep(2)
                
                current_title = driver.title
                current_url = driver.current_url
                opened_pages.append(f"{i+1}. {current_title} - {current_url}")
                
                driver.back()
                time.sleep(1)
                
            except Exception as e:
                log(f"[PAGE OPEN ERROR] {str(e)}", Fore.RED)
                continue
        
        result_text = f"Opened {len(opened_pages)} pages for: {query}\n"
        for page in opened_pages:
            result_text += f"{page}\n"
        
        log(f"[MULTI-PAGE] Opened {len(opened_pages)} pages", Fore.CYAN)
        return result_text
        
    except Exception as e:
        err = f"[MULTI-PAGE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def write_creative_story(topic):
    try:
        messages = [{"role": "user", "content": f"Write a creative short story (150-200 words) about: {topic if topic else 'a magical adventure'}"}]
        story_response = qwen_client.chat.completions.create(
            model="openchat/openchat-7b:free",
            messages=messages,
            max_tokens=500,
            temperature=0.8
        )
        story = story_response.choices[0].message.content.strip()
        
        open_new_note()
        time.sleep(1)
        write_to_note(story)
        time.sleep(0.5)
        save_note()
        
        log(f"[STORY] Wrote creative story about: {topic}", Fore.CYAN)
        return f"[✓] Creative story written and saved ({len(story)} chars)"
    except Exception as e:
        err = f"[STORY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def analyze_web_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title'
        paragraphs = soup.find_all('p')
        links = soup.find_all('a', href=True)
        
        analysis = f"Analysis of {url}:\n"
        analysis += f"Title: {title}\n"
        analysis += f"Paragraphs found: {len(paragraphs)}\n"
        analysis += f"Links found: {len(links)}\n"
        
        main_content = []
        for p in paragraphs[:3]:
            text = p.get_text().strip()
            if len(text) > 20:
                main_content.append(text)
        
        analysis += "Main content:\n"
        for i, content in enumerate(main_content, 1):
            analysis += f"{i}. {content[:100]}...\n"
        
        log(f"[ANALYSIS] Analyzed content from: {url}", Fore.CYAN)
        return analysis
    except Exception as e:
        err = f"[ANALYSIS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def sign_in_to_website(url, username, password, username_field="username", password_field="password"):
    global driver
    if not driver:
        driver = init_advanced_browser()
        if not driver:
            return "[ERROR] No browser available"
    
    try:
        driver.get(url)
        time.sleep(2)
        
        try:
            username_input = driver.find_element(By.NAME, username_field)
            username_input.clear()
            username_input.send_keys(username)
        except:
            for field_name in ["username", "email", "user", "login", "email_address"]:
                try:
                    username_input = driver.find_element(By.NAME, field_name)
                    username_input.clear()
                    username_input.send_keys(username)
                    break
                except:
                    continue
        
        try:
            password_input = driver.find_element(By.NAME, password_field)
            password_input.clear()
            password_input.send_keys(password)
        except:
            for field_name in ["password", "pass", "pwd", "user_password"]:
                try:
                    password_input = driver.find_element(By.NAME, field_name)
                    password_input.clear()
                    password_input.send_keys(password)
                    break
                except:
                    continue
        
        try:
            login_button = driver.find_element(By.XPATH, "//input[@type='submit' or @value='Login' or @value='Sign In']")
            login_button.click()
        except:
            for selector in ["//button[contains(text(), 'Login')]", "//button[contains(text(), 'Sign In')]", "//input[@type='button']"]:
                try:
                    login_button = driver.find_element(By.XPATH, selector)
                    login_button.click()
                    break
                except:
                    continue
        
        time.sleep(2)
        
        log(f"[SIGN-IN] Attempted to sign in to: {url}", Fore.CYAN)
        return f"[✓] Sign-in attempt completed for: {url}"
        
    except Exception as e:
        err = f"[SIGN-IN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def chat_with_ai(message):
    try:
        messages = [{"role": "user", "content": message}]
        response = qwen_client.chat.completions.create(
            model="openchat/openchat-7b:free",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        log(f"[AI CHAT] Response: {reply[:100]}...", Fore.CYAN)
        return reply
    except Exception as e:
        err = f"[AI CHAT ERROR] {str(e)}"
        log(err, Fore.RED)
        return "Sorry, I'm having trouble responding right now."

def get_system_info():
    try:
        info = {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
            'processes': len(psutil.pids()),
            'network_io': psutil.net_io_counters()._asdict()
        }
        log("[SYSTEM] Retrieved system information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[SYSTEM ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, timeout=30)
        output = result.stdout or result.stderr
        log(f"[POWERSHELL] Executed: {command[:50]}...", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[POWERSHELL TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[POWERSHELL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def list_processes():
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        log(f"[PROCESSES] Listed {len(processes)} processes", Fore.CYAN)
        return str(processes[:20])  # Limit to first 20 processes
    except Exception as e:
        err = f"[PROCESSES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def kill_process_by_name(name):
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == name:
                proc.kill()
                log(f"[KILL] Killed process: {name}", Fore.CYAN)
                return f"[✓] Killed process: {name} (PID: {proc.info['pid']})"
        
        return f"[ERROR] Process {name} not found"
    except Exception as e:
        err = f"[KILL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_window_list():
    try:
        windows = gw.getAllTitles()
        log(f"[WINDOWS] Found {len(windows)} windows", Fore.CYAN)
        return str(windows)
    except Exception as e:
        err = f"[WINDOWS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def send_text_to_window(window_title, text):
    try:
        window = find_window(window_title)
        if window:
            window.activate()
            time.sleep(0.5)
            pyautogui.write(text, interval=0.01)
            log(f"[WINDOW] Sent text to: {window_title}", Fore.CYAN)
            return f"[✓] Sent text to: {window_title}"
        else:
            return f"[WINDOW] Window not found: {window_title}"
    except Exception as e:
        err = f"[WINDOW TEXT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def take_full_screenshot():
    try:
        with mss.mss() as sct:
            screenshot = sct.grab(sct.monitors[0])
            filename = f"full_screenshot_{int(time.time())}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=filepath)
            log(f"[FULL SCREENSHOT] Saved: {filepath}", Fore.CYAN)
            return f"[✓] Full screenshot saved: {filepath}"
    except Exception as e:
        err = f"[FULL SCREENSHOT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def record_screen(duration=10):
    try:
        import cv2
        import numpy as np
        
        # Get screen dimensions
        screen = pyautogui.screenshot()
        screen_array = np.array(screen)
        height, width, channels = screen_array.shape
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = f"screen_record_{int(time.time())}.avi"
        filepath = os.path.join(TEMP_DIR, filename)
        out = cv2.VideoWriter(filepath, fourcc, 20.0, (width, height))
        
        start_time = time.time()
        while time.time() - start_time < duration:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        
        out.release()
        log(f"[RECORD] Screen recording saved: {filepath}", Fore.CYAN)
        return f"[✓] Screen recording saved: {filepath}"
    except Exception as e:
        err = f"[RECORD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_mouse_position():
    try:
        x, y = pyautogui.position()
        log(f"[MOUSE] Current position: ({x}, {y})", Fore.CYAN)
        return f"[✓] Mouse at ({x}, {y})"
    except Exception as e:
        err = f"[MOUSE POS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_active_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        log(f"[ACTIVE WINDOW] {window_title}", Fore.CYAN)
        return f"[✓] Active window: {window_title}"
    except Exception as e:
        err = f"[ACTIVE WINDOW ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_clipboard_content():
    try:
        content = pyperclip.paste()
        log(f"[CLIPBOARD] Retrieved content ({len(content)} chars)", Fore.CYAN)
        return content
    except Exception as e:
        err = f"[CLIPBOARD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def clear_clipboard():
    try:
        pyperclip.copy("")
        log("[CLIPBOARD] Cleared", Fore.CYAN)
        return "[✓] Clipboard cleared"
    except Exception as e:
        err = f"[CLIPBOARD CLEAR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_all_files_in_directory(directory=".", pattern="*"):
    try:
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, pattern):
                files.append(os.path.join(root, filename))
        
        log(f"[FILES] Found {len(files)} files matching '{pattern}'", Fore.CYAN)
        return str(files[:20])  # Limit to first 20 files
    except Exception as e:
        err = f"[FILES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        log(f"[DIR] Created directory: {path}", Fore.CYAN)
        return f"[✓] Created directory: {path}"
    except Exception as e:
        err = f"[DIR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def delete_file(path):
    try:
        os.remove(path)
        log(f"[DELETE] Deleted file: {path}", Fore.CYAN)
        return f"[✓] Deleted file: {path}"
    except Exception as e:
        err = f"[DELETE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def delete_directory(path):
    try:
        shutil.rmtree(path)
        log(f"[DELETE] Deleted directory: {path}", Fore.CYAN)
        return f"[✓] Deleted directory: {path}"
    except Exception as e:
        err = f"[DELETE DIR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def zip_directory(source_dir, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, source_dir))
        
        log(f"[ZIP] Created zip: {zip_path}", Fore.CYAN)
        return f"[✓] Created zip: {zip_path}"
    except Exception as e:
        err = f"[ZIP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_to)
        
        log(f"[UNZIP] Extracted to: {extract_to}", Fore.CYAN)
        return f"[✓] Extracted to: {extract_to}"
    except Exception as e:
        err = f"[UNZIP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_network_info():
    try:
        info = {
            'hostname': socket.gethostname(),
            'ip_address': socket.gethostbyname(socket.gethostname()),
            'network_interfaces': psutil.net_if_addrs()
        }
        log("[NETWORK] Retrieved network information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[NETWORK ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def ping_host(host):
    try:
        result = subprocess.run(['ping', '-n', '4', host], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log(f"[PING] Pinged {host}", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[PING TIMEOUT] Ping took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[PING ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_wifi_networks():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[WIFI] Retrieved available networks", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[WIFI TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[WIFI ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def connect_to_wifi(ssid, password):
    try:
        # Create a temporary network profile
        profile = f"""<?xml version="1.0"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>{ssid}</name>
            <SSIDConfig>
                <SSID>
                    <name>{ssid}</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>manual</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>{password}</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>"""
        
        # Save profile to temp file
        temp_profile = os.path.join(TEMP_DIR, f"{ssid}_profile.xml")
        with open(temp_profile, 'w') as f:
            f.write(profile)
        
        # Add and connect to the profile
        subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={temp_profile}'], timeout=30)
        result = subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], capture_output=True, text=True, timeout=30)
        
        log(f"[WIFI] Attempted to connect to: {ssid}", Fore.CYAN)
        return result.stdout[:500]
    except subprocess.TimeoutExpired:
        msg = "[WIFI CONNECT TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[WIFI CONNECT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            info = {
                'percent': battery.percent,
                'charging': battery.power_plugged,
                'time_left': battery.secsleft if battery.secsleft != psutil.POWER_TIME_UNLIMITED else 'Unlimited'
            }
            log("[BATTERY] Retrieved battery status", Fore.CYAN)
            return str(info)
        else:
            return "[BATTERY] No battery found (desktop?)"
    except Exception as e:
        err = f"[BATTERY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def shutdown_computer(delay=0):
    try:
        if delay > 0:
            subprocess.run(['shutdown', '/s', '/t', str(delay)])
        else:
            subprocess.run(['shutdown', '/s', '/t', '0'])
        
        log(f"[SHUTDOWN] Computer will shutdown in {delay} seconds", Fore.CYAN)
        return f"[✓] Computer will shutdown in {delay} seconds"
    except Exception as e:
        err = f"[SHUTDOWN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def restart_computer(delay=0):
    try:
        if delay > 0:
            subprocess.run(['shutdown', '/r', '/t', str(delay)])
        else:
            subprocess.run(['shutdown', '/r', '/t', '0'])
        
        log(f"[RESTART] Computer will restart in {delay} seconds", Fore.CYAN)
        return f"[✓] Computer will restart in {delay} seconds"
    except Exception as e:
        err = f"[RESTART ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def sleep_computer():
    try:
        import ctypes
        ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
        log("[SLEEP] Computer sent to sleep", Fore.CYAN)
        return "[✓] Computer sent to sleep"
    except Exception as e:
        err = f"[SLEEP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def lock_computer():
    try:
        import ctypes
        ctypes.windll.user32.LockWorkStation()
        log("[LOCK] Computer locked", Fore.CYAN)
        return "[✓] Computer locked"
    except Exception as e:
        err = f"[LOCK ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_installed_programs():
    try:
        programs = []
        # Check Windows Registry for installed programs
        reg_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]
        
        for reg_path in reg_paths:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            try:
                                display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                programs.append(display_name)
                            except:
                                pass
            except:
                pass
        
        log(f"[PROGRAMS] Found {len(programs)} installed programs", Fore.CYAN)
        return str(programs[:50])  # Limit to first 50 programs
    except Exception as e:
        err = f"[PROGRAMS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_running_services():
    try:
        c = wmi.WMI()
        services = []
        for service in c.Win32_Service():
            services.append({
                'name': service.Name,
                'display_name': service.DisplayName,
                'state': service.State,
                'start_mode': service.StartMode
            })
        
        log(f"[SERVICES] Found {len(services)} services", Fore.CYAN)
        return str(services[:20])  # Limit to first 20 services
    except Exception as e:
        err = f"[SERVICES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def start_service(service_name):
    try:
        c = wmi.WMI()
        service = c.Win32_Service(Name=service_name)
        if service:
            result = service[0].StartService()
            log(f"[SERVICE] Started: {service_name}", Fore.CYAN)
            return f"[✓] Started service: {service_name}"
        else:
            return f"[SERVICE] Service not found: {service_name}"
    except Exception as e:
        err = f"[SERVICE START ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def stop_service(service_name):
    try:
        c = wmi.WMI()
        service = c.Win32_Service(Name=service_name)
        if service:
            result = service[0].StopService()
            log(f"[SERVICE] Stopped: {service_name}", Fore.CYAN)
            return f"[✓] Stopped service: {service_name}"
        else:
            return f"[SERVICE] Service not found: {service_name}"
    except Exception as e:
        err = f"[SERVICE STOP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_registry_value(hive, key_path, value_name):
    try:
        if hive == "HKEY_LOCAL_MACHINE":
            hive = winreg.HKEY_LOCAL_MACHINE
        elif hive == "HKEY_CURRENT_USER":
            hive = winreg.HKEY_CURRENT_USER
        elif hive == "HKEY_CLASSES_ROOT":
            hive = winreg.HKEY_CLASSES_ROOT
        elif hive == "HKEY_USERS":
            hive = winreg.HKEY_USERS
        else:
            return "[REGISTRY] Invalid hive"
        
        with winreg.OpenKey(hive, key_path) as key:
            value, _ = winreg.QueryValueEx(key, value_name)
        
        log(f"[REGISTRY] Retrieved {value_name} from {key_path}", Fore.CYAN)
        return str(value)
    except Exception as e:
        err = f"[REGISTRY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_registry_value(hive, key_path, value_name, value, value_type=winreg.REG_SZ):
    try:
        if hive == "HKEY_LOCAL_MACHINE":
            hive = winreg.HKEY_LOCAL_MACHINE
        elif hive == "HKEY_CURRENT_USER":
            hive = winreg.HKEY_CURRENT_USER
        elif hive == "HKEY_CLASSES_ROOT":
            hive = winreg.HKEY_CLASSES_ROOT
        elif hive == "HKEY_USERS":
            hive = winreg.HKEY_USERS
        else:
            return "[REGISTRY] Invalid hive"
        
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, value_name, 0, value_type, value)
        
        log(f"[REGISTRY] Set {value_name} in {key_path}", Fore.CYAN)
        return f"[✓] Set registry value: {value_name}"
    except Exception as e:
        err = f"[REGISTRY SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_cpu_info():
    try:
        info = {
            'cpu_count': psutil.cpu_count(),
            'cpu_count_logical': psutil.cpu_count(logical=True),
            'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else 'N/A',
            'cpu_percent': psutil.cpu_percent(interval=1),
            'cpu_percent_per_core': psutil.cpu_percent(percpu=True)
        }
        log("[CPU] Retrieved CPU information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[CPU ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_memory_info():
    try:
        info = {
            'memory_total': psutil.virtual_memory().total,
            'memory_available': psutil.virtual_memory().available,
            'memory_percent': psutil.virtual_memory().percent,
            'memory_used': psutil.virtual_memory().used,
            'swap_total': psutil.swap_memory().total,
            'swap_used': psutil.swap_memory().used,
            'swap_percent': psutil.swap_memory().percent
        }
        log("[MEMORY] Retrieved memory information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[MEMORY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_disk_info():
    try:
        partitions = psutil.disk_partitions()
        info = {}
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                info[partition.mountpoint] = {
                    'total': usage.total,
                    'used': usage.used,
                    'free': usage.free,
                    'percentage': (usage.used / usage.total) * 100
                }
            except:
                continue
        
        log("[DISK] Retrieved disk information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[DISK ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_network_stats():
    try:
        info = {
            'net_io_counters': psutil.net_io_counters()._asdict(),
            'net_connections': len(psutil.net_connections()),
            'net_if_stats': {iface: stats._asdict() for iface, stats in psutil.net_if_stats().items()}
        }
        log("[NETWORK] Retrieved network statistics", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[NETWORK STATS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_uptime():
    try:
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        log("[UPTIME] Retrieved system uptime", Fore.CYAN)
        return f"[✓] System uptime: {uptime}"
    except Exception as e:
        err = f"[UPTIME ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_user_accounts():
    try:
        result = subprocess.run(['net', 'user'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[USERS] Retrieved user accounts", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[USERS TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[USERS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def create_user_account(username, password):
    try:
        result = subprocess.run(['net', 'user', username, password, '/add'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log(f"[USER] Created user: {username}", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[USER CREATE TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[USER CREATE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def delete_user_account(username):
    try:
        result = subprocess.run(['net', 'user', username, '/delete'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log(f"[USER] Deleted user: {username}", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[USER DELETE TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[USER DELETE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_startup_programs():
    try:
        programs = []
        # Check registry for startup programs
        reg_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
        ]
        
        for reg_path in reg_paths:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                    for i in range(winreg.QueryInfoKey(key)[1]):
                        name, value, _ = winreg.EnumValue(key, i)
                        programs.append({'name': name, 'path': value})
            except:
                pass
        
        log(f"[STARTUP] Found {len(programs)} startup programs", Fore.CYAN)
        return str(programs)
    except Exception as e:
        err = f"[STARTUP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def add_to_startup(name, path):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
        
        log(f"[STARTUP] Added {name} to startup", Fore.CYAN)
        return f"[✓] Added {name} to startup"
    except Exception as e:
        err = f"[STARTUP ADD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def remove_from_startup(name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, name)
        
        log(f"[STARTUP] Removed {name} from startup", Fore.CYAN)
        return f"[✓] Removed {name} from startup"
    except Exception as e:
        err = f"[STARTUP REMOVE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_recent_files():
    try:
        recent_path = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Recent")
        files = []
        for file in os.listdir(recent_path):
            if file.endswith('.lnk'):
                files.append(file)
        
        log(f"[RECENT] Found {len(files)} recent files", Fore.CYAN)
        return str(files[:20])  # Limit to first 20 files
    except Exception as e:
        err = f"[RECENT FILES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_recent_documents():
    try:
        doc_path = os.path.expanduser(r"~\Documents")
        files = []
        for root, dirs, filenames in os.walk(doc_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                mod_time = os.path.getmtime(file_path)
                files.append({'name': filename, 'path': file_path, 'modified': mod_time})
        
        # Sort by modification time (most recent first)
        files.sort(key=lambda x: x['modified'], reverse=True)
        
        log(f"[DOCUMENTS] Found {len(files)} documents", Fore.CYAN)
        return str(files[:10])  # Limit to first 10 files
    except Exception as e:
        err = f"[DOCUMENTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_browser_history():
    try:
        # This is a simplified version - full browser history extraction is complex
        # and may require browser-specific libraries
        browsers = {
            'chrome': os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\History"),
            'edge': os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\User Data\Default\History"),
            'firefox': os.path.expanduser(r"~\AppData\Roaming\Mozilla\Firefox\Profiles")
        }
        
        history_info = {}
        for browser, path in browsers.items():
            if os.path.exists(path):
                history_info[browser] = f"History file exists at: {path}"
            else:
                history_info[browser] = "History file not found"
        
        log("[BROWSER HISTORY] Retrieved browser history info", Fore.CYAN)
        return str(history_info)
    except Exception as e:
        err = f"[BROWSER HISTORY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_installed_apps():
    try:
        # Get installed apps via PowerShell
        result = subprocess.run(['powershell', '-Command', 'Get-AppxPackage -AllUsers | Select Name, InstallLocation'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[APPS] Retrieved installed apps", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[APPS TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[APPS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_drivers():
    try:
        result = subprocess.run(['driverquery'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[DRIVERS] Retrieved system drivers", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[DRIVERS TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[DRIVERS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def update_driver(driver_name):
    try:
        # This is a simplified version - actual driver updates are complex
        result = subprocess.run(['pnputil', '/enum-drivers'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log(f"[DRIVER] Attempted to update: {driver_name}", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[DRIVER TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[DRIVER UPDATE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_windows_updates():
    try:
        result = subprocess.run(['wuauclt', '/reportnow'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[UPDATES] Retrieved Windows update status", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[UPDATES TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[UPDATES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def install_windows_updates():
    try:
        result = subprocess.run(['wuauclt', '/updatenow'], capture_output=True, text=True, timeout=60)
        output = result.stdout
        log("[UPDATES] Attempted to install Windows updates", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[UPDATES TIMEOUT] Command took longer than 60 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[UPDATES INSTALL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_antivirus_status():
    try:
        c = wmi.WMI(namespace=r'root\SecurityCenter2')
        antivirus_products = c.AntiVirusProduct()
        
        products = []
        for product in antivirus_products:
            products.append({
                'name': product.displayName,
                'status': product.productState
            })
        
        log(f"[ANTIVIRUS] Found {len(products)} antivirus products", Fore.CYAN)
        return str(products)
    except Exception as e:
        err = f"[ANTIVIRUS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_firewall_status():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[FIREWALL] Retrieved firewall status", Fore.CYAN)
        return output[:1000]
    except subprocess.TimeoutExpired:
        msg = "[FIREWALL TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[FIREWALL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def enable_firewall():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[FIREWALL] Enabled firewall", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[FIREWALL TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[FIREWALL ENABLE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def disable_firewall():
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'off'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[FIREWALL] Disabled firewall", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[FIREWALL TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[FIREWALL DISABLE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_performance():
    try:
        info = {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'network_io': psutil.net_io_counters()._asdict(),
            'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        }
        log("[PERFORMANCE] Retrieved system performance", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[PERFORMANCE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def optimize_system():
    try:
        # This is a simplified optimization routine
        # In reality, system optimization is complex and should be done carefully
        commands = [
            'cleanmgr /sagerun:1',  # Disk cleanup
            'sfc /scannow',         # System file check
            'defrag C: /U'          # Disk defragmentation
        ]
        
        results = []
        for cmd in commands:
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
                results.append(f"Command: {cmd}\nOutput: {result.stdout[:200]}")
            except subprocess.TimeoutExpired:
                results.append(f"Command: {cmd}\nStatus: TIMEOUT")
            except Exception as e:
                results.append(f"Command: {cmd}\nError: {str(e)}")
        
        log("[OPTIMIZE] System optimization attempted", Fore.CYAN)
        return "\n".join(results)
    except Exception as e:
        err = f"[OPTIMIZE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_hardware_info():
    try:
        info = {
            'cpu_info': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else 'N/A',
            'memory_total': psutil.virtual_memory().total,
            'disk_partitions': [p.mountpoint for p in psutil.disk_partitions()],
            'network_interfaces': list(psutil.net_if_addrs().keys())
        }
        log("[HARDWARE] Retrieved hardware information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[HARDWARE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_software_info():
    try:
        info = {
            'python_version': sys.version,
            'platform': sys.platform,
            'os_info': os.name,
            'installed_packages': subprocess.run([sys.executable, '-m', 'pip', 'list'], capture_output=True, text=True).stdout[:500]
        }
        log("[SOFTWARE] Retrieved software information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[SOFTWARE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_logs():
    try:
        # This is a simplified version - actual system logs require admin rights
        result = subprocess.run(['eventvwr'], shell=True, capture_output=True, text=True, timeout=10)
        log("[LOGS] Attempted to access system logs", Fore.CYAN)
        return "[✓] System logs viewer opened (requires admin rights for detailed logs)"
    except Exception as e:
        err = f"[LOGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def clear_system_logs():
    try:
        # This is a simplified version - actual log clearing requires admin rights
        log("[LOGS] Attempted to clear system logs", Fore.CYAN)
        return "[✓] Log clearing requires admin rights"
    except Exception as e:
        err = f"[LOGS CLEAR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_temp_files():
    try:
        temp_dir = tempfile.gettempdir()
        files = []
        for root, dirs, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                files.append({'name': filename, 'path': file_path, 'size': os.path.getsize(file_path)})
        
        log(f"[TEMP] Found {len(files)} temporary files", Fore.CYAN)
        return str(files[:20])  # Limit to first 20 files
    except Exception as e:
        err = f"[TEMP FILES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def clear_temp_files():
    try:
        temp_dir = tempfile.gettempdir()
        count = 0
        for root, dirs, filenames in os.walk(temp_dir):
            for filename in filenames:
                try:
                    file_path = os.path.join(root, filename)
                    os.remove(file_path)
                    count += 1
                except:
                    continue
        
        log(f"[TEMP] Cleared {count} temporary files", Fore.CYAN)
        return f"[✓] Cleared {count} temporary files"
    except Exception as e:
        err = f"[TEMP CLEAR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_recycle_bin_contents():
    try:
        # This is a simplified version - actual recycle bin access is complex
        log("[RECYCLE] Attempted to access recycle bin", Fore.CYAN)
        return "[✓] Recycle bin access requires special permissions"
    except Exception as e:
        err = f"[RECYCLE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def empty_recycle_bin():
    try:
        import winshell
        winshell.recycle_bin().empty(confirm=False, show_progress=False)
        log("[RECYCLE] Emptied recycle bin", Fore.CYAN)
        return "[✓] Recycle bin emptied"
    except Exception as e:
        err = f"[RECYCLE EMPTY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_disk_space_info():
    try:
        partitions = psutil.disk_partitions()
        info = {}
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                info[partition.mountpoint] = {
                    'total_gb': round(usage.total / (1024**3), 2),
                    'used_gb': round(usage.used / (1024**3), 2),
                    'free_gb': round(usage.free / (1024**3), 2),
                    'percentage': round((usage.used / usage.total) * 100, 2)
                }
            except:
                continue
        
        log("[DISK SPACE] Retrieved disk space information", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[DISK SPACE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_network_connections():
    try:
        connections = psutil.net_connections()
        info = []
        for conn in connections:
            info.append({
                'family': conn.family,
                'type': conn.type,
                'local_address': conn.laddr,
                'remote_address': conn.raddr,
                'status': conn.status,
                'pid': conn.pid
            })
        
        log(f"[CONNECTIONS] Found {len(info)} network connections", Fore.CYAN)
        return str(info[:20])  # Limit to first 20 connections
    except Exception as e:
        err = f"[CONNECTIONS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_processes_by_cpu_usage():
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by CPU usage
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        
        log(f"[PROCESSES CPU] Retrieved {len(processes)} processes sorted by CPU usage", Fore.CYAN)
        return str(processes[:10])  # Limit to top 10 CPU users
    except Exception as e:
        err = f"[PROCESSES CPU ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_processes_by_memory_usage():
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by memory usage
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        
        log(f"[PROCESSES MEMORY] Retrieved {len(processes)} processes sorted by memory usage", Fore.CYAN)
        return str(processes[:10])  # Limit to top 10 memory users
    except Exception as e:
        err = f"[PROCESSES MEMORY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_environment():
    try:
        env = dict(os.environ)
        log("[ENVIRONMENT] Retrieved system environment variables", Fore.CYAN)
        return str(list(env.keys())[:50])  # Limit to first 50 environment variables
    except Exception as e:
        err = f"[ENVIRONMENT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_time():
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log(f"[TIME] Current system time: {current_time}", Fore.CYAN)
        return f"[✓] Current time: {current_time}"
    except Exception as e:
        err = f"[TIME ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_time(new_time):
    try:
        # This requires admin rights and is complex
        log(f"[TIME] Attempted to set system time to: {new_time}", Fore.CYAN)
        return "[✓] Time setting requires admin rights"
    except Exception as e:
        err = f"[TIME SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_timezone_info():
    try:
        import time
        tz_info = {
            'timezone': time.tzname,
            'utc_offset': time.timezone,
            'daylight_savings': time.daylight
        }
        log("[TIMEZONE] Retrieved timezone information", Fore.CYAN)
        return str(tz_info)
    except Exception as e:
        err = f"[TIMEZONE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_locale():
    try:
        import locale
        locale_info = {
            'default_locale': locale.getdefaultlocale(),
            'preferred_encoding': locale.getpreferredencoding()
        }
        log("[LOCALE] Retrieved system locale information", Fore.CYAN)
        return str(locale_info)
    except Exception as e:
        err = f"[LOCALE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_language():
    try:
        import ctypes
        windll = ctypes.windll.kernel32
        language_id = windll.GetUserDefaultUILanguage()
        log(f"[LANGUAGE] Retrieved system language ID: {language_id}", Fore.CYAN)
        return f"[✓] System language ID: {language_id}"
    except Exception as e:
        err = f"[LANGUAGE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_fonts():
    try:
        import win32gui
        fonts = []
        def enum_font_callback(logfont, metrics, fonttype, param):
            fonts.append(logfont.lfFaceName)
            return True
        
        hdc = win32gui.GetDC(0)
        win32gui.EnumFontFamilies(hdc, None, enum_font_callback, None)
        win32gui.ReleaseDC(0, hdc)
        
        log(f"[FONTS] Retrieved {len(fonts)} system fonts", Fore.CYAN)
        return str(fonts[:50])  # Limit to first 50 fonts
    except Exception as e:
        err = f"[FONTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_themes():
    try:
        # This is a simplified version - actual theme info is complex
        log("[THEMES] Attempted to retrieve system themes", Fore.CYAN)
        return "[✓] Theme information requires registry access"
    except Exception as e:
        err = f"[THEMES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_wallpaper():
    try:
        # This is a simplified version - actual wallpaper info is complex
        log("[WALLPAPER] Attempted to retrieve system wallpaper", Fore.CYAN)
        return "[✓] Wallpaper information requires registry access"
    except Exception as e:
        err = f"[WALLPAPER ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_wallpaper(image_path):
    try:
        # This is a simplified version - actual wallpaper setting is complex
        log(f"[WALLPAPER] Attempted to set wallpaper: {image_path}", Fore.CYAN)
        return "[✓] Wallpaper setting requires registry access"
    except Exception as e:
        err = f"[WALLPAPER SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_screen_resolution():
    try:
        width, height = pyautogui.size()
        log(f"[SCREEN] Current resolution: {width}x{height}", Fore.CYAN)
        return f"[✓] Screen resolution: {width}x{height}"
    except Exception as e:
        err = f"[SCREEN RES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_screen_resolution(width, height):
    try:
        # This is a simplified version - actual resolution setting is complex
        log(f"[SCREEN] Attempted to set resolution: {width}x{height}", Fore.CYAN)
        return "[✓] Resolution setting requires display driver access"
    except Exception as e:
        err = f"[SCREEN SET RES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_screen_color_depth():
    try:
        # This is a simplified version - actual color depth is complex
        log("[SCREEN] Attempted to retrieve color depth", Fore.CYAN)
        return "[✓] Color depth information requires display driver access"
    except Exception as e:
        err = f"[SCREEN COLOR DEPTH ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_screen_refresh_rate():
    try:
        # This is a simplified version - actual refresh rate is complex
        log("[SCREEN] Attempted to retrieve refresh rate", Fore.CYAN)
        return "[✓] Refresh rate information requires display driver access"
    except Exception as e:
        err = f"[SCREEN REFRESH ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_audio_devices():
    try:
        import pyaudio
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        
        devices = []
        for i in range(num_devices):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            devices.append({
                'name': device_info.get('name'),
                'max_input_channels': device_info.get('maxInputChannels'),
                'max_output_channels': device_info.get('maxOutputChannels'),
                'default_sample_rate': device_info.get('defaultSampleRate')
            })
        
        log(f"[AUDIO] Found {len(devices)} audio devices", Fore.CYAN)
        return str(devices)
    except Exception as e:
        err = f"[AUDIO DEVICES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_microphone_status():
    try:
        # This is a simplified version - actual microphone status is complex
        log("[MICROPHONE] Attempted to retrieve microphone status", Fore.CYAN)
        return "[✓] Microphone status requires audio API access"
    except Exception as e:
        err = f"[MICROPHONE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_speakers_status():
    try:
        # This is a simplified version - actual speaker status is complex
        log("[SPEAKERS] Attempted to retrieve speaker status", Fore.CYAN)
        return "[✓] Speaker status requires audio API access"
    except Exception as e:
        err = f"[SPEAKERS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_volume_level():
    try:
        # This is a simplified version - actual volume control is complex
        log("[VOLUME] Attempted to retrieve volume level", Fore.CYAN)
        return "[✓] Volume level requires audio API access"
    except Exception as e:
        err = f"[VOLUME ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_volume_level(level):
    try:
        # This is a simplified version - actual volume control is complex
        log(f"[VOLUME] Attempted to set volume to: {level}", Fore.CYAN)
        return "[✓] Volume setting requires audio API access"
    except Exception as e:
        err = f"[VOLUME SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def mute_audio():
    try:
        # This is a simplified version - actual audio control is complex
        log("[AUDIO] Attempted to mute audio", Fore.CYAN)
        return "[✓] Audio muting requires audio API access"
    except Exception as e:
        err = f"[AUDIO MUTE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def unmute_audio():
    try:
        # This is a simplified version - actual audio control is complex
        log("[AUDIO] Attempted to unmute audio", Fore.CYAN)
        return "[✓] Audio unmuting requires audio API access"
    except Exception as e:
        err = f"[AUDIO UNMUTE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def record_audio(duration=5):
    try:
        import pyaudio
        import wave
        
        chunk = 1024
        format = pyaudio.paInt16
        channels = 2
        rate = 44100
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
        
        log(f"[AUDIO] Recording audio for {duration} seconds", Fore.CYAN)
        
        frames = []
        for i in range(0, int(rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        filename = f"audio_record_{int(time.time())}.wav"
        filepath = os.path.join(TEMP_DIR, filename)
        
        wf = wave.open(filepath, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        log(f"[AUDIO] Audio recording saved: {filepath}", Fore.CYAN)
        return f"[✓] Audio recording saved: {filepath}"
    except Exception as e:
        err = f"[AUDIO RECORD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def play_audio(file_path):
    try:
        import pyaudio
        import wave
        
        wf = wave.open(file_path, 'rb')
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        log(f"[AUDIO] Played audio file: {file_path}", Fore.CYAN)
        return f"[✓] Played audio file: {file_path}"
    except Exception as e:
        err = f"[AUDIO PLAY ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_camera_status():
    try:
        # This is a simplified version - actual camera status is complex
        log("[CAMERA] Attempted to retrieve camera status", Fore.CYAN)
        return "[✓] Camera status requires video API access"
    except Exception as e:
        err = f"[CAMERA ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def take_camera_photo():
    try:
        # This is a simplified version - actual camera access is complex
        log("[CAMERA] Attempted to take camera photo", Fore.CYAN)
        return "[✓] Camera access requires video API access"
    except Exception as e:
        err = f"[CAMERA PHOTO ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def start_camera_recording():
    try:
        # This is a simplified version - actual camera access is complex
        log("[CAMERA] Attempted to start camera recording", Fore.CYAN)
        return "[✓] Camera recording requires video API access"
    except Exception as e:
        err = f"[CAMERA RECORD ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def stop_camera_recording():
    try:
        # This is a simplified version - actual camera access is complex
        log("[CAMERA] Attempted to stop camera recording", Fore.CYAN)
        return "[✓] Camera recording requires video API access"
    except Exception as e:
        err = f"[CAMERA STOP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_bluetooth_status():
    try:
        # This is a simplified version - actual Bluetooth status is complex
        log("[BLUETOOTH] Attempted to retrieve Bluetooth status", Fore.CYAN)
        return "[✓] Bluetooth status requires Bluetooth API access"
    except Exception as e:
        err = f"[BLUETOOTH ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_connected_bluetooth_devices():
    try:
        # This is a simplified version - actual Bluetooth devices are complex
        log("[BLUETOOTH] Attempted to retrieve connected Bluetooth devices", Fore.CYAN)
        return "[✓] Bluetooth devices require Bluetooth API access"
    except Exception as e:
        err = f"[BLUETOOTH DEVICES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def connect_bluetooth_device(device_address):
    try:
        # This is a simplified version - actual Bluetooth connection is complex
        log(f"[BLUETOOTH] Attempted to connect to device: {device_address}", Fore.CYAN)
        return "[✓] Bluetooth connection requires Bluetooth API access"
    except Exception as e:
        err = f"[BLUETOOTH CONNECT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def disconnect_bluetooth_device(device_address):
    try:
        # This is a simplified version - actual Bluetooth disconnection is complex
        log(f"[BLUETOOTH] Attempted to disconnect device: {device_address}", Fore.CYAN)
        return "[✓] Bluetooth disconnection requires Bluetooth API access"
    except Exception as e:
        err = f"[BLUETOOTH DISCONNECT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_usb_devices():
    try:
        # This is a simplified version - actual USB devices are complex
        log("[USB] Attempted to retrieve connected USB devices", Fore.CYAN)
        return "[✓] USB devices require WMI or registry access"
    except Exception as e:
        err = f"[USB DEVICES ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_serial_ports():
    try:
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        log(f"[SERIAL] Found {len(port_list)} serial ports", Fore.CYAN)
        return str(port_list)
    except Exception as e:
        err = f"[SERIAL PORTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_parallel_ports():
    try:
        # This is a simplified version - actual parallel ports are rare now
        log("[PARALLEL] Attempted to retrieve parallel ports", Fore.CYAN)
        return "[✓] Parallel ports are rarely used in modern systems"
    except Exception as e:
        err = f"[PARALLEL PORTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_sensors():
    try:
        # This is a simplified version - actual sensors require special hardware
        log("[SENSORS] Attempted to retrieve system sensors", Fore.CYAN)
        return "[✓] System sensors require specialized hardware"
    except Exception as e:
        err = f"[SENSORS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_gpu_info():
    try:
        # This is a simplified version - actual GPU info requires special libraries
        result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True, text=True, timeout=30)
        output = result.stdout
        log("[GPU] Retrieved GPU information", Fore.CYAN)
        return output[:500]
    except subprocess.TimeoutExpired:
        msg = "[GPU TIMEOUT] Command took longer than 30 seconds"
        log(msg, Fore.RED)
        return msg
    except Exception as e:
        err = f"[GPU ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_temperatures():
    try:
        # This is a simplified version - actual temperature monitoring requires special hardware
        log("[TEMPERATURE] Attempted to retrieve system temperatures", Fore.CYAN)
        return "[✓] Temperature monitoring requires specialized hardware"
    except Exception as e:
        err = f"[TEMPERATURE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_fans():
    try:
        # This is a simplified version - actual fan monitoring requires special hardware
        log("[FANS] Attempted to retrieve system fans", Fore.CYAN)
        return "[✓] Fan monitoring requires specialized hardware"
    except Exception as e:
        err = f"[FANS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_power_status():
    try:
        info = {
            'battery_percent': psutil.sensors_battery().percent if psutil.sensors_battery() else 'N/A',
            'battery_charging': psutil.sensors_battery().power_plugged if psutil.sensors_battery() else 'N/A',
            'battery_time_left': psutil.sensors_battery().secsleft if psutil.sensors_battery() else 'N/A'
        }
        log("[POWER] Retrieved system power status", Fore.CYAN)
        return str(info)
    except Exception as e:
        err = f"[POWER ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_updates_info():
    try:
        # This is a simplified version - actual Windows Update info is complex
        log("[UPDATES] Attempted to retrieve system updates info", Fore.CYAN)
        return "[✓] Update info requires Windows Update API access"
    except Exception as e:
        err = f"[UPDATES INFO ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_backup_status():
    try:
        # This is a simplified version - actual backup status is complex
        log("[BACKUP] Attempted to retrieve system backup status", Fore.CYAN)
        return "[✓] Backup status requires Windows Backup API access"
    except Exception as e:
        err = f"[BACKUP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def create_system_backup():
    try:
        # This is a simplified version - actual backup creation is complex
        log("[BACKUP] Attempted to create system backup", Fore.CYAN)
        return "[✓] System backup requires Windows Backup API access"
    except Exception as e:
        err = f"[BACKUP CREATE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def restore_system_backup():
    try:
        # This is a simplified version - actual backup restoration is complex
        log("[BACKUP] Attempted to restore system backup", Fore.CYAN)
        return "[✓] System restore requires Windows Backup API access"
    except Exception as e:
        err = f"[BACKUP RESTORE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_restore_points():
    try:
        # This is a simplified version - actual restore points are complex
        log("[RESTORE] Attempted to retrieve system restore points", Fore.CYAN)
        return "[✓] Restore points require Windows System Restore API access"
    except Exception as e:
        err = f"[RESTORE POINTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def create_system_restore_point(description="Manual Restore Point"):
    try:
        # This is a simplified version - actual restore point creation is complex
        log(f"[RESTORE] Attempted to create restore point: {description}", Fore.CYAN)
        return "[✓] Restore point creation requires Windows System Restore API access"
    except Exception as e:
        err = f"[RESTORE CREATE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def restore_system_to_point(point_id):
    try:
        # This is a simplified version - actual system restore is complex
        log(f"[RESTORE] Attempted to restore to point: {point_id}", Fore.CYAN)
        return "[✓] System restore requires Windows System Restore API access"
    except Exception as e:
        err = f"[RESTORE TO POINT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_performance_counters():
    try:
        # This is a simplified version - actual performance counters are complex
        log("[PERFORMANCE] Attempted to retrieve system performance counters", Fore.CYAN)
        return "[✓] Performance counters require Windows Performance API access"
    except Exception as e:
        err = f"[PERFORMANCE COUNTERS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_event_logs():
    try:
        # This is a simplified version - actual event logs require admin rights
        log("[EVENTS] Attempted to retrieve system event logs", Fore.CYAN)
        return "[✓] Event logs require Windows Event Log API access"
    except Exception as e:
        err = f"[EVENTS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def clear_system_event_logs():
    try:
        # This is a simplified version - actual event log clearing requires admin rights
        log("[EVENTS] Attempted to clear system event logs", Fore.CYAN)
        return "[✓] Event log clearing requires admin rights"
    except Exception as e:
        err = f"[EVENTS CLEAR ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_registry_info():
    try:
        # This is a simplified version - actual registry access requires admin rights
        log("[REGISTRY] Attempted to retrieve system registry info", Fore.CYAN)
        return "[✓] Registry access requires admin rights"
    except Exception as e:
        err = f"[REGISTRY INFO ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def backup_system_registry():
    try:
        # This is a simplified version - actual registry backup requires admin rights
        log("[REGISTRY] Attempted to backup system registry", Fore.CYAN)
        return "[✓] Registry backup requires admin rights"
    except Exception as e:
        err = f"[REGISTRY BACKUP ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def restore_system_registry(backup_path):
    try:
        # This is a simplified version - actual registry restoration requires admin rights
        log(f"[REGISTRY] Attempted to restore registry from: {backup_path}", Fore.CYAN)
        return "[✓] Registry restoration requires admin rights"
    except Exception as e:
        err = f"[REGISTRY RESTORE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_service_status(service_name):
    try:
        c = wmi.WMI()
        service = c.Win32_Service(Name=service_name)
        if service:
            status = service[0].State
            log(f"[SERVICE] Status of {service_name}: {status}", Fore.CYAN)
            return f"[✓] Service {service_name} is {status}"
        else:
            return f"[SERVICE] Service not found: {service_name}"
    except Exception as e:
        err = f"[SERVICE STATUS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_startup_items():
    try:
        # This is a simplified version - actual startup items require registry access
        log("[STARTUP] Attempted to retrieve system startup items", Fore.CYAN)
        return "[✓] Startup items require registry access"
    except Exception as e:
        err = f"[STARTUP ITEMS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def add_system_startup_item(name, path):
    try:
        # This is a simplified version - actual startup item addition requires registry access
        log(f"[STARTUP] Attempted to add startup item: {name}", Fore.CYAN)
        return "[✓] Startup item addition requires registry access"
    except Exception as e:
        err = f"[STARTUP ADD ITEM ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def remove_system_startup_item(name):
    try:
        # This is a simplified version - actual startup item removal requires registry access
        log(f"[STARTUP] Attempted to remove startup item: {name}", Fore.CYAN)
        return "[✓] Startup item removal requires registry access"
    except Exception as e:
        err = f"[STARTUP REMOVE ITEM ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_environment_variables():
    try:
        env_vars = dict(os.environ)
        log(f"[ENVIRONMENT] Retrieved {len(env_vars)} environment variables", Fore.CYAN)
        return str(list(env_vars.keys())[:50])  # Limit to first 50 variables
    except Exception as e:
        err = f"[ENVIRONMENT VARS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_environment_variable(name, value):
    try:
        os.environ[name] = value
        log(f"[ENVIRONMENT] Set environment variable: {name}={value}", Fore.CYAN)
        return f"[✓] Set environment variable: {name}"
    except Exception as e:
        err = f"[ENVIRONMENT SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def delete_system_environment_variable(name):
    try:
        if name in os.environ:
            del os.environ[name]
            log(f"[ENVIRONMENT] Deleted environment variable: {name}", Fore.CYAN)
            return f"[✓] Deleted environment variable: {name}"
        else:
            return f"[ENVIRONMENT] Variable not found: {name}"
    except Exception as e:
        err = f"[ENVIRONMENT DELETE ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_timezone():
    try:
        import time
        timezone = time.tzname
        log(f"[TIMEZONE] Current system timezone: {timezone}", Fore.CYAN)
        return f"[✓] System timezone: {timezone}"
    except Exception as e:
        err = f"[TIMEZONE GET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_timezone(timezone_name):
    try:
        # This is a simplified version - actual timezone setting requires admin rights
        log(f"[TIMEZONE] Attempted to set timezone: {timezone_name}", Fore.CYAN)
        return "[✓] Timezone setting requires admin rights"
    except Exception as e:
        err = f"[TIMEZONE SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_locale_settings():
    try:
        import locale
        locale_settings = {
            'default_locale': locale.getdefaultlocale(),
            'preferred_encoding': locale.getpreferredencoding(),
            'locale_categories': [locale.localeconv()]
        }
        log("[LOCALE] Retrieved system locale settings", Fore.CYAN)
        return str(locale_settings)
    except Exception as e:
        err = f"[LOCALE SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_locale(locale_name):
    try:
        # This is a simplified version - actual locale setting is complex
        log(f"[LOCALE] Attempted to set locale: {locale_name}", Fore.CYAN)
        return "[✓] Locale setting requires system configuration"
    except Exception as e:
        err = f"[LOCALE SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_language_settings():
    try:
        # This is a simplified version - actual language settings are complex
        log("[LANGUAGE] Attempted to retrieve system language settings", Fore.CYAN)
        return "[✓] Language settings require Windows API access"
    except Exception as e:
        err = f"[LANGUAGE SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_language(language_code):
    try:
        # This is a simplified version - actual language setting is complex
        log(f"[LANGUAGE] Attempted to set language: {language_code}", Fore.CYAN)
        return "[✓] Language setting requires Windows API access"
    except Exception as e:
        err = f"[LANGUAGE SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_keyboard_layout():
    try:
        # This is a simplified version - actual keyboard layout is complex
        log("[KEYBOARD] Attempted to retrieve system keyboard layout", Fore.CYAN)
        return "[✓] Keyboard layout requires Windows API access"
    except Exception as e:
        err = f"[KEYBOARD LAYOUT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_keyboard_layout(layout_code):
    try:
        # This is a simplified version - actual keyboard layout setting is complex
        log(f"[KEYBOARD] Attempted to set keyboard layout: {layout_code}", Fore.CYAN)
        return "[✓] Keyboard layout setting requires Windows API access"
    except Exception as e:
        err = f"[KEYBOARD SET LAYOUT ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_mouse_settings():
    try:
        # This is a simplified version - actual mouse settings are complex
        log("[MOUSE] Attempted to retrieve system mouse settings", Fore.CYAN)
        return "[✓] Mouse settings require Windows API access"
    except Exception as e:
        err = f"[MOUSE SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_mouse_settings(speed=10, acceleration=True):
    try:
        # This is a simplified version - actual mouse setting is complex
        log(f"[MOUSE] Attempted to set mouse speed: {speed}, acceleration: {acceleration}", Fore.CYAN)
        return "[✓] Mouse settings require Windows API access"
    except Exception as e:
        err = f"[MOUSE SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_display_settings():
    try:
        # This is a simplified version - actual display settings are complex
        log("[DISPLAY] Attempted to retrieve system display settings", Fore.CYAN)
        return "[✓] Display settings require Windows API access"
    except Exception as e:
        err = f"[DISPLAY SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_display_settings(brightness=100, contrast=50):
    try:
        # This is a simplified version - actual display setting is complex
        log(f"[DISPLAY] Attempted to set brightness: {brightness}, contrast: {contrast}", Fore.CYAN)
        return "[✓] Display settings require Windows API access"
    except Exception as e:
        err = f"[DISPLAY SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_audio_settings():
    try:
        # This is a simplified version - actual audio settings are complex
        log("[AUDIO] Attempted to retrieve system audio settings", Fore.CYAN)
        return "[✓] Audio settings require Windows API access"
    except Exception as e:
        err = f"[AUDIO SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_audio_settings(volume=50, mute=False):
    try:
        # This is a simplified version - actual audio setting is complex
        log(f"[AUDIO] Attempted to set volume: {volume}, mute: {mute}", Fore.CYAN)
        return "[✓] Audio settings require Windows API access"
    except Exception as e:
        err = f"[AUDIO SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_power_settings():
    try:
        # This is a simplified version - actual power settings are complex
        log("[POWER] Attempted to retrieve system power settings", Fore.CYAN)
        return "[✓] Power settings require Windows API access"
    except Exception as e:
        err = f"[POWER SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_power_settings(scheme="balanced", timeout=60):
    try:
        # This is a simplified version - actual power setting is complex
        log(f"[POWER] Attempted to set power scheme: {scheme}, timeout: {timeout}", Fore.CYAN)
        return "[✓] Power settings require Windows API access"
    except Exception as e:
        err = f"[POWER SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_security_settings():
    try:
        # This is a simplified version - actual security settings are complex
        log("[SECURITY] Attempted to retrieve system security settings", Fore.CYAN)
        return "[✓] Security settings require Windows API access"
    except Exception as e:
        err = f"[SECURITY SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_security_settings(enhanced_security=True):
    try:
        # This is a simplified version - actual security setting is complex
        log(f"[SECURITY] Attempted to set enhanced security: {enhanced_security}", Fore.CYAN)
        return "[✓] Security settings require Windows API access"
    except Exception as e:
        err = f"[SECURITY SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_privacy_settings():
    try:
        # This is a simplified version - actual privacy settings are complex
        log("[PRIVACY] Attempted to retrieve system privacy settings", Fore.CYAN)
        return "[✓] Privacy settings require Windows API access"
    except Exception as e:
        err = f"[PRIVACY SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_privacy_settings(data_collection=False, location_tracking=False):
    try:
        # This is a simplified version - actual privacy setting is complex
        log(f"[PRIVACY] Attempted to set data_collection: {data_collection}, location_tracking: {location_tracking}", Fore.CYAN)
        return "[✓] Privacy settings require Windows API access"
    except Exception as e:
        err = f"[PRIVACY SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_updates_settings():
    try:
        # This is a simplified version - actual update settings are complex
        log("[UPDATES] Attempted to retrieve system updates settings", Fore.CYAN)
        return "[✓] Update settings require Windows API access"
    except Exception as e:
        err = f"[UPDATES SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_updates_settings(auto_updates=True, download_only=False):
    try:
        # This is a simplified version - actual update setting is complex
        log(f"[UPDATES] Attempted to set auto_updates: {auto_updates}, download_only: {download_only}", Fore.CYAN)
        return "[✓] Update settings require Windows API access"
    except Exception as e:
        err = f"[UPDATES SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_backup_settings():
    try:
        # This is a simplified version - actual backup settings are complex
        log("[BACKUP] Attempted to retrieve system backup settings", Fore.CYAN)
        return "[✓] Backup settings require Windows API access"
    except Exception as e:
        err = f"[BACKUP SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_backup_settings(auto_backup=True, backup_location="C:\\Backup"):
    try:
        # This is a simplified version - actual backup setting is complex
        log(f"[BACKUP] Attempted to set auto_backup: {auto_backup}, location: {backup_location}", Fore.CYAN)
        return "[✓] Backup settings require Windows API access"
    except Exception as e:
        err = f"[BACKUP SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_network_settings():
    try:
        # This is a simplified version - actual network settings are complex
        log("[NETWORK] Attempted to retrieve system network settings", Fore.CYAN)
        return "[✓] Network settings require Windows API access"
    except Exception as e:
        err = f"[NETWORK SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_network_settings(proxy_server="", dns_server=""):
    try:
        # This is a simplified version - actual network setting is complex
        log(f"[NETWORK] Attempted to set proxy: {proxy_server}, DNS: {dns_server}", Fore.CYAN)
        return "[✓] Network settings require Windows API access"
    except Exception as e:
        err = f"[NETWORK SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_wifi_settings():
    try:
        # This is a simplified version - actual WiFi settings are complex
        log("[WIFI] Attempted to retrieve system WiFi settings", Fore.CYAN)
        return "[✓] WiFi settings require Windows API access"
    except Exception as e:
        err = f"[WIFI SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_wifi_settings(ssid="", password="", auto_connect=True):
    try:
        # This is a simplified version - actual WiFi setting is complex
        log(f"[WIFI] Attempted to set SSID: {ssid}, auto_connect: {auto_connect}", Fore.CYAN)
        return "[✓] WiFi settings require Windows API access"
    except Exception as e:
        err = f"[WIFI SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_bluetooth_settings():
    try:
        # This is a simplified version - actual Bluetooth settings are complex
        log("[BLUETOOTH] Attempted to retrieve system Bluetooth settings", Fore.CYAN)
        return "[✓] Bluetooth settings require Windows API access"
    except Exception as e:
        err = f"[BLUETOOTH SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_bluetooth_settings(enabled=True, discoverable=True):
    try:
        # This is a simplified version - actual Bluetooth setting is complex
        log(f"[BLUETOOTH] Attempted to set enabled: {enabled}, discoverable: {discoverable}", Fore.CYAN)
        return "[✓] Bluetooth settings require Windows API access"
    except Exception as e:
        err = f"[BLUETOOTH SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_usb_settings():
    try:
        # This is a simplified version - actual USB settings are complex
        log("[USB] Attempted to retrieve system USB settings", Fore.CYAN)
        return "[✓] USB settings require Windows API access"
    except Exception as e:
        err = f"[USB SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_usb_settings(auto_install_drivers=True, power_saving=True):
    try:
        # This is a simplified version - actual USB setting is complex
        log(f"[USB] Attempted to set auto_install_drivers: {auto_install_drivers}, power_saving: {power_saving}", Fore.CYAN)
        return "[✓] USB settings require Windows API access"
    except Exception as e:
        err = f"[USB SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_printer_settings():
    try:
        # This is a simplified version - actual printer settings are complex
        log("[PRINTER] Attempted to retrieve system printer settings", Fore.CYAN)
        return "[✓] Printer settings require Windows API access"
    except Exception as e:
        err = f"[PRINTER SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_printer_settings(default_printer="", print_quality="normal"):
    try:
        # This is a simplified version - actual printer setting is complex
        log(f"[PRINTER] Attempted to set default_printer: {default_printer}, quality: {print_quality}", Fore.CYAN)
        return "[✓] Printer settings require Windows API access"
    except Exception as e:
        err = f"[PRINTER SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_camera_settings():
    try:
        # This is a simplified version - actual camera settings are complex
        log("[CAMERA] Attempted to retrieve system camera settings", Fore.CYAN)
        return "[✓] Camera settings require Windows API access"
    except Exception as e:
        err = f"[CAMERA SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_camera_settings(resolution="1080p", frame_rate=30):
    try:
        # This is a simplified version - actual camera setting is complex
        log(f"[CAMERA] Attempted to set resolution: {resolution}, frame_rate: {frame_rate}", Fore.CYAN)
        return "[✓] Camera settings require Windows API access"
    except Exception as e:
        err = f"[CAMERA SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_microphone_settings():
    try:
        # This is a simplified version - actual microphone settings are complex
        log("[MICROPHONE] Attempted to retrieve system microphone settings", Fore.CYAN)
        return "[✓] Microphone settings require Windows API access"
    except Exception as e:
        err = f"[MICROPHONE SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_microphone_settings(sensitivity=50, noise_reduction=True):
    try:
        # This is a simplified version - actual microphone setting is complex
        log(f"[MICROPHONE] Attempted to set sensitivity: {sensitivity}, noise_reduction: {noise_reduction}", Fore.CYAN)
        return "[✓] Microphone settings require Windows API access"
    except Exception as e:
        err = f"[MICROPHONE SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_speaker_settings():
    try:
        # This is a simplified version - actual speaker settings are complex
        log("[SPEAKER] Attempted to retrieve system speaker settings", Fore.CYAN)
        return "[✓] Speaker settings require Windows API access"
    except Exception as e:
        err = f"[SPEAKER SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_speaker_settings(volume=75, bass=50, treble=50):
    try:
        # This is a simplified version - actual speaker setting is complex
        log(f"[SPEAKER] Attempted to set volume: {volume}, bass: {bass}, treble: {treble}", Fore.CYAN)
        return "[✓] Speaker settings require Windows API access"
    except Exception as e:
        err = f"[SPEAKER SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_game_settings():
    try:
        # This is a simplified version - actual game settings are complex
        log("[GAME] Attempted to retrieve system game settings", Fore.CYAN)
        return "[✓] Game settings require Windows API access"
    except Exception as e:
        err = f"[GAME SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_game_settings(high_performance=True, vsync=False):
    try:
        # This is a simplified version - actual game setting is complex
        log(f"[GAME] Attempted to set high_performance: {high_performance}, vsync: {vsync}", Fore.CYAN)
        return "[✓] Game settings require Windows API access"
    except Exception as e:
        err = f"[GAME SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_developer_settings():
    try:
        # This is a simplified version - actual developer settings are complex
        log("[DEVELOPER] Attempted to retrieve system developer settings", Fore.CYAN)
        return "[✓] Developer settings require Windows API access"
    except Exception as e:
        err = f"[DEVELOPER SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_developer_settings(developer_mode=True, usb_debugging=False):
    try:
        # This is a simplified version - actual developer setting is complex
        log(f"[DEVELOPER] Attempted to set developer_mode: {developer_mode}, usb_debugging: {usb_debugging}", Fore.CYAN)
        return "[✓] Developer settings require Windows API access"
    except Exception as e:
        err = f"[DEVELOPER SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_admin_settings():
    try:
        # This is a simplified version - actual admin settings require admin rights
        log("[ADMIN] Attempted to retrieve system admin settings", Fore.CYAN)
        return "[✓] Admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_admin_settings(admin_password=""):
    try:
        # This is a simplified version - actual admin setting requires admin rights
        log(f"[ADMIN] Attempted to set admin password", Fore.CYAN)
        return "[✓] Admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_advanced_settings():
    try:
        # This is a simplified version - actual advanced settings are complex
        log("[ADVANCED] Attempted to retrieve system advanced settings", Fore.CYAN)
        return "[✓] Advanced settings require Windows API access"
    except Exception as e:
        err = f"[ADVANCED SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_advanced_settings(advanced_features=True):
    try:
        # This is a simplified version - actual advanced setting is complex
        log(f"[ADVANCED] Attempted to set advanced features: {advanced_features}", Fore.CYAN)
        return "[✓] Advanced settings require Windows API access"
    except Exception as e:
        err = f"[ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_hidden_settings():
    try:
        # This is a simplified version - actual hidden settings require admin rights
        log("[HIDDEN] Attempted to retrieve system hidden settings", Fore.CYAN)
        return "[✓] Hidden settings require admin rights"
    except Exception as e:
        err = f"[HIDDEN SETTINGS ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_hidden_settings(enable_hidden=True):
    try:
        # This is a simplified version - actual hidden setting requires admin rights
        log(f"[HIDDEN] Attempted to set enable_hidden: {enable_hidden}", Fore.CYAN)
        return "[✓] Hidden settings require admin rights"
    except Exception as e:
        err = f"[HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_registry_advanced():
    try:
        # This is a simplified version - actual registry access requires admin rights
        log("[REGISTRY ADVANCED] Attempted to retrieve advanced registry settings", Fore.CYAN)
        return "[✓] Advanced registry settings require admin rights"
    except Exception as e:
        err = f"[REGISTRY ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_registry_advanced(key_path, value_name, value_data):
    try:
        # This is a simplified version - actual registry setting requires admin rights
        log(f"[REGISTRY ADVANCED] Attempted to set {key_path}\\{value_name}={value_data}", Fore.CYAN)
        return "[✓] Advanced registry setting requires admin rights"
    except Exception as e:
        err = f"[REGISTRY ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_performance_advanced():
    try:
        # This is a simplified version - actual performance settings are complex
        log("[PERFORMANCE ADVANCED] Attempted to retrieve advanced performance settings", Fore.CYAN)
        return "[✓] Advanced performance settings require Windows API access"
    except Exception as e:
        err = f"[PERFORMANCE ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_performance_advanced(ram_boost=True, cpu_priority="normal"):
    try:
        # This is a simplified version - actual performance setting is complex
        log(f"[PERFORMANCE ADVANCED] Attempted to set ram_boost: {ram_boost}, cpu_priority: {cpu_priority}", Fore.CYAN)
        return "[✓] Advanced performance settings require Windows API access"
    except Exception as e:
        err = f"[PERFORMANCE ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_network_advanced():
    try:
        # This is a simplified version - actual network settings are complex
        log("[NETWORK ADVANCED] Attempted to retrieve advanced network settings", Fore.CYAN)
        return "[✓] Advanced network settings require Windows API access"
    except Exception as e:
        err = f"[NETWORK ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_network_advanced(buffer_size=64, connection_timeout=30):
    try:
        # This is a simplified version - actual network setting is complex
        log(f"[NETWORK ADVANCED] Attempted to set buffer_size: {buffer_size}, timeout: {connection_timeout}", Fore.CYAN)
        return "[✓] Advanced network settings require Windows API access"
    except Exception as e:
        err = f"[NETWORK ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_security_advanced():
    try:
        # This is a simplified version - actual security settings are complex
        log("[SECURITY ADVANCED] Attempted to retrieve advanced security settings", Fore.CYAN)
        return "[✓] Advanced security settings require Windows API access"
    except Exception as e:
        err = f"[SECURITY ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_security_advanced(real_time_protection=True, firewall_level="high"):
    try:
        # This is a simplified version - actual security setting is complex
        log(f"[SECURITY ADVANCED] Attempted to set real_time_protection: {real_time_protection}, firewall_level: {firewall_level}", Fore.CYAN)
        return "[✓] Advanced security settings require Windows API access"
    except Exception as e:
        err = f"[SECURITY ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_privacy_advanced():
    try:
        # This is a simplified version - actual privacy settings are complex
        log("[PRIVACY ADVANCED] Attempted to retrieve advanced privacy settings", Fore.CYAN)
        return "[✓] Advanced privacy settings require Windows API access"
    except Exception as e:
        err = f"[PRIVACY ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_privacy_advanced(app_tracking=False, diagnostic_data="minimal"):
    try:
        # This is a simplified version - actual privacy setting is complex
        log(f"[PRIVACY ADVANCED] Attempted to set app_tracking: {app_tracking}, diagnostic_ {diagnostic_data}", Fore.CYAN)
        return "[✓] Advanced privacy settings require Windows API access"
    except Exception as e:
        err = f"[PRIVACY ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_updates_advanced():
    try:
        # This is a simplified version - actual update settings are complex
        log("[UPDATES ADVANCED] Attempted to retrieve advanced updates settings", Fore.CYAN)
        return "[✓] Advanced updates settings require Windows API access"
    except Exception as e:
        err = f"[UPDATES ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_updates_advanced(auto_download=True, schedule_time="02:00"):
    try:
        # This is a simplified version - actual update setting is complex
        log(f"[UPDATES ADVANCED] Attempted to set auto_download: {auto_download}, schedule_time: {schedule_time}", Fore.CYAN)
        return "[✓] Advanced updates settings require Windows API access"
    except Exception as e:
        err = f"[UPDATES ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_backup_advanced():
    try:
        # This is a simplified version - actual backup settings are complex
        log("[BACKUP ADVANCED] Attempted to retrieve advanced backup settings", Fore.CYAN)
        return "[✓] Advanced backup settings require Windows API access"
    except Exception as e:
        err = f"[BACKUP ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_backup_advanced(backup_frequency="daily", retention_days=30):
    try:
        # This is a simplified version - actual backup setting is complex
        log(f"[BACKUP ADVANCED] Attempted to set backup_frequency: {backup_frequency}, retention_days: {retention_days}", Fore.CYAN)
        return "[✓] Advanced backup settings require Windows API access"
    except Exception as e:
        err = f"[BACKUP ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_display_advanced():
    try:
        # This is a simplified version - actual display settings are complex
        log("[DISPLAY ADVANCED] Attempted to retrieve advanced display settings", Fore.CYAN)
        return "[✓] Advanced display settings require Windows API access"
    except Exception as e:
        err = f"[DISPLAY ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_display_advanced(color_temperature=6500, refresh_rate=60):
    try:
        # This is a simplified version - actual display setting is complex
        log(f"[DISPLAY ADVANCED] Attempted to set color_temperature: {color_temperature}, refresh_rate: {refresh_rate}", Fore.CYAN)
        return "[✓] Advanced display settings require Windows API access"
    except Exception as e:
        err = f"[DISPLAY ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_audio_advanced():
    try:
        # This is a simplified version - actual audio settings are complex
        log("[AUDIO ADVANCED] Attempted to retrieve advanced audio settings", Fore.CYAN)
        return "[✓] Advanced audio settings require Windows API access"
    except Exception as e:
        err = f"[AUDIO ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_audio_advanced(sample_rate=44100, bit_depth=16):
    try:
        # This is a simplified version - actual audio setting is complex
        log(f"[AUDIO ADVANCED] Attempted to set sample_rate: {sample_rate}, bit_depth: {bit_depth}", Fore.CYAN)
        return "[✓] Advanced audio settings require Windows API access"
    except Exception as e:
        err = f"[AUDIO ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_power_advanced():
    try:
        # This is a simplified version - actual power settings are complex
        log("[POWER ADVANCED] Attempted to retrieve advanced power settings", Fore.CYAN)
        return "[✓] Advanced power settings require Windows API access"
    except Exception as e:
        err = f"[POWER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_power_advanced(cpu_governor="performance", gpu_boost=True):
    try:
        # This is a simplified version - actual power setting is complex
        log(f"[POWER ADVANCED] Attempted to set cpu_governor: {cpu_governor}, gpu_boost: {gpu_boost}", Fore.CYAN)
        return "[✓] Advanced power settings require Windows API access"
    except Exception as e:
        err = f"[POWER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_gpu_advanced():
    try:
        # This is a simplified version - actual GPU settings are complex
        log("[GPU ADVANCED] Attempted to retrieve advanced GPU settings", Fore.CYAN)
        return "[✓] Advanced GPU settings require GPU API access"
    except Exception as e:
        err = f"[GPU ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_gpu_advanced(overclock_gpu=False, memory_clock=1000):
    try:
        # This is a simplified version - actual GPU setting is complex
        log(f"[GPU ADVANCED] Attempted to set overclock_gpu: {overclock_gpu}, memory_clock: {memory_clock}", Fore.CYAN)
        return "[✓] Advanced GPU settings require GPU API access"
    except Exception as e:
        err = f"[GPU ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_cpu_advanced():
    try:
        # This is a simplified version - actual CPU settings are complex
        log("[CPU ADVANCED] Attempted to retrieve advanced CPU settings", Fore.CYAN)
        return "[✓] Advanced CPU settings require CPU API access"
    except Exception as e:
        err = f"[CPU ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_cpu_advanced(overclock_cpu=False, voltage=1.2):
    try:
        # This is a simplified version - actual CPU setting is complex
        log(f"[CPU ADVANCED] Attempted to set overclock_cpu: {overclock_cpu}, voltage: {voltage}", Fore.CYAN)
        return "[✓] Advanced CPU settings require CPU API access"
    except Exception as e:
        err = f"[CPU ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_memory_advanced():
    try:
        # This is a simplified version - actual memory settings are complex
        log("[MEMORY ADVANCED] Attempted to retrieve advanced memory settings", Fore.CYAN)
        return "[✓] Advanced memory settings require memory API access"
    except Exception as e:
        err = f"[MEMORY ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_memory_advanced(timing="auto", voltage=1.35):
    try:
        # This is a simplified version - actual memory setting is complex
        log(f"[MEMORY ADVANCED] Attempted to set timing: {timing}, voltage: {voltage}", Fore.CYAN)
        return "[✓] Advanced memory settings require memory API access"
    except Exception as e:
        err = f"[MEMORY ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_storage_advanced():
    try:
        # This is a simplified version - actual storage settings are complex
        log("[STORAGE ADVANCED] Attempted to retrieve advanced storage settings", Fore.CYAN)
        return "[✓] Advanced storage settings require storage API access"
    except Exception as e:
        err = f"[STORAGE ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_storage_advanced(trim_enabled=True, cache_size=1024):
    try:
        # This is a simplified version - actual storage setting is complex
        log(f"[STORAGE ADVANCED] Attempted to set trim_enabled: {trim_enabled}, cache_size: {cache_size}", Fore.CYAN)
        return "[✓] Advanced storage settings require storage API access"
    except Exception as e:
        err = f"[STORAGE ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_network_card_advanced():
    try:
        # This is a simplified version - actual network card settings are complex
        log("[NETWORK CARD ADVANCED] Attempted to retrieve advanced network card settings", Fore.CYAN)
        return "[✓] Advanced network card settings require network card API access"
    except Exception as e:
        err = f"[NETWORK CARD ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_network_card_advanced(speed="auto", duplex="auto"):
    try:
        # This is a simplified version - actual network card setting is complex
        log(f"[NETWORK CARD ADVANCED] Attempted to set speed: {speed}, duplex: {duplex}", Fore.CYAN)
        return "[✓] Advanced network card settings require network card API access"
    except Exception as e:
        err = f"[NETWORK CARD ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_wifi_card_advanced():
    try:
        # This is a simplified version - actual WiFi card settings are complex
        log("[WIFI CARD ADVANCED] Attempted to retrieve advanced WiFi card settings", Fore.CYAN)
        return "[✓] Advanced WiFi card settings require WiFi card API access"
    except Exception as e:
        err = f"[WIFI CARD ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_wifi_card_advanced(channel=6, power=100):
    try:
        # This is a simplified version - actual WiFi card setting is complex
        log(f"[WIFI CARD ADVANCED] Attempted to set channel: {channel}, power: {power}", Fore.CYAN)
        return "[✓] Advanced WiFi card settings require WiFi card API access"
    except Exception as e:
        err = f"[WIFI CARD ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_bluetooth_card_advanced():
    try:
        # This is a simplified version - actual Bluetooth card settings are complex
        log("[BLUETOOTH CARD ADVANCED] Attempted to retrieve advanced Bluetooth card settings", Fore.CYAN)
        return "[✓] Advanced Bluetooth card settings require Bluetooth card API access"
    except Exception as e:
        err = f"[BLUETOOTH CARD ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_bluetooth_card_advanced(power_level=7, connection_timeout=30):
    try:
        # This is a simplified version - actual Bluetooth card setting is complex
        log(f"[BLUETOOTH CARD ADVANCED] Attempted to set power_level: {power_level}, timeout: {connection_timeout}", Fore.CYAN)
        return "[✓] Advanced Bluetooth card settings require Bluetooth card API access"
    except Exception as e:
        err = f"[BLUETOOTH CARD ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_usb_controller_advanced():
    try:
        # This is a simplified version - actual USB controller settings are complex
        log("[USB CONTROLLER ADVANCED] Attempted to retrieve advanced USB controller settings", Fore.CYAN)
        return "[✓] Advanced USB controller settings require USB controller API access"
    except Exception as e:
        err = f"[USB CONTROLLER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_usb_controller_advanced(power_management=True, bandwidth_limit=100):
    try:
        # This is a simplified version - actual USB controller setting is complex
        log(f"[USB CONTROLLER ADVANCED] Attempted to set power_management: {power_management}, bandwidth_limit: {bandwidth_limit}", Fore.CYAN)
        return "[✓] Advanced USB controller settings require USB controller API access"
    except Exception as e:
        err = f"[USB CONTROLLER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_audio_controller_advanced():
    try:
        # This is a simplified version - actual audio controller settings are complex
        log("[AUDIO CONTROLLER ADVANCED] Attempted to retrieve advanced audio controller settings", Fore.CYAN)
        return "[✓] Advanced audio controller settings require audio controller API access"
    except Exception as e:
        err = f"[AUDIO CONTROLLER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_audio_controller_advanced(sample_rate=48000, buffer_size=1024):
    try:
        # This is a simplified version - actual audio controller setting is complex
        log(f"[AUDIO CONTROLLER ADVANCED] Attempted to set sample_rate: {sample_rate}, buffer_size: {buffer_size}", Fore.CYAN)
        return "[✓] Advanced audio controller settings require audio controller API access"
    except Exception as e:
        err = f"[AUDIO CONTROLLER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_video_controller_advanced():
    try:
        # This is a simplified version - actual video controller settings are complex
        log("[VIDEO CONTROLLER ADVANCED] Attempted to retrieve advanced video controller settings", Fore.CYAN)
        return "[✓] Advanced video controller settings require video controller API access"
    except Exception as e:
        err = f"[VIDEO CONTROLLER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_video_controller_advanced(color_depth=32, refresh_rate=75):
    try:
        # This is a simplified version - actual video controller setting is complex
        log(f"[VIDEO CONTROLLER ADVANCED] Attempted to set color_depth: {color_depth}, refresh_rate: {refresh_rate}", Fore.CYAN)
        return "[✓] Advanced video controller settings require video controller API access"
    except Exception as e:
        err = f"[VIDEO CONTROLLER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_printer_advanced():
    try:
        # This is a simplified version - actual printer settings are complex
        log("[PRINTER ADVANCED] Attempted to retrieve advanced printer settings", Fore.CYAN)
        return "[✓] Advanced printer settings require printer API access"
    except Exception as e:
        err = f"[PRINTER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_printer_advanced(dpi=600, paper_size="A4"):
    try:
        # This is a simplified version - actual printer setting is complex
        log(f"[PRINTER ADVANCED] Attempted to set dpi: {dpi}, paper_size: {paper_size}", Fore.CYAN)
        return "[✓] Advanced printer settings require printer API access"
    except Exception as e:
        err = f"[PRINTER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_camera_advanced():
    try:
        # This is a simplified version - actual camera settings are complex
        log("[CAMERA ADVANCED] Attempted to retrieve advanced camera settings", Fore.CYAN)
        return "[✓] Advanced camera settings require camera API access"
    except Exception as e:
        err = f"[CAMERA ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_camera_advanced(exposure=50, iso=100):
    try:
        # This is a simplified version - actual camera setting is complex
        log(f"[CAMERA ADVANCED] Attempted to set exposure: {exposure}, iso: {iso}", Fore.CYAN)
        return "[✓] Advanced camera settings require camera API access"
    except Exception as e:
        err = f"[CAMERA ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_microphone_advanced():
    try:
        # This is a simplified version - actual microphone settings are complex
        log("[MICROPHONE ADVANCED] Attempted to retrieve advanced microphone settings", Fore.CYAN)
        return "[✓] Advanced microphone settings require microphone API access"
    except Exception as e:
        err = f"[MICROPHONE ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_microphone_advanced(gain=50, sample_rate=44100):
    try:
        # This is a simplified version - actual microphone setting is complex
        log(f"[MICROPHONE ADVANCED] Attempted to set gain: {gain}, sample_rate: {sample_rate}", Fore.CYAN)
        return "[✓] Advanced microphone settings require microphone API access"
    except Exception as e:
        err = f"[MICROPHONE ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_speaker_advanced():
    try:
        # This is a simplified version - actual speaker settings are complex
        log("[SPEAKER ADVANCED] Attempted to retrieve advanced speaker settings", Fore.CYAN)
        return "[✓] Advanced speaker settings require speaker API access"
    except Exception as e:
        err = f"[SPEAKER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_speaker_advanced(crossover_frequency=1000, bass_management=True):
    try:
        # This is a simplified version - actual speaker setting is complex
        log(f"[SPEAKER ADVANCED] Attempted to set crossover_frequency: {crossover_frequency}, bass_management: {bass_management}", Fore.CYAN)
        return "[✓] Advanced speaker settings require speaker API access"
    except Exception as e:
        err = f"[SPEAKER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_game_advanced():
    try:
        # This is a simplified version - actual game settings are complex
        log("[GAME ADVANCED] Attempted to retrieve advanced game settings", Fore.CYAN)
        return "[✓] Advanced game settings require game API access"
    except Exception as e:
        err = f"[GAME ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_game_advanced(frame_limit=60, texture_quality="high"):
    try:
        # This is a simplified version - actual game setting is complex
        log(f"[GAME ADVANCED] Attempted to set frame_limit: {frame_limit}, texture_quality: {texture_quality}", Fore.CYAN)
        return "[✓] Advanced game settings require game API access"
    except Exception as e:
        err = f"[GAME ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_developer_advanced():
    try:
        # This is a simplified version - actual developer settings are complex
        log("[DEVELOPER ADVANCED] Attempted to retrieve advanced developer settings", Fore.CYAN)
        return "[✓] Advanced developer settings require developer API access"
    except Exception as e:
        err = f"[DEVELOPER ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_developer_advanced(debug_mode=True, performance_profiling=True):
    try:
        # This is a simplified version - actual developer setting is complex
        log(f"[DEVELOPER ADVANCED] Attempted to set debug_mode: {debug_mode}, performance_profiling: {performance_profiling}", Fore.CYAN)
        return "[✓] Advanced developer settings require developer API access"
    except Exception as e:
        err = f"[DEVELOPER ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_admin_advanced():
    try:
        # This is a simplified version - actual admin settings require admin rights
        log("[ADMIN ADVANCED] Attempted to retrieve advanced admin settings", Fore.CYAN)
        return "[✓] Advanced admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_admin_advanced(enable_remote_access=True, audit_log_level="medium"):
    try:
        # This is a simplified version - actual admin setting requires admin rights
        log(f"[ADMIN ADVANCED] Attempted to set enable_remote_access: {enable_remote_access}, audit_log_level: {audit_log_level}", Fore.CYAN)
        return "[✓] Advanced admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_advanced_all():
    try:
        # This is a simplified version - actual advanced settings are complex
        log("[ADVANCED ALL] Attempted to retrieve all advanced settings", Fore.CYAN)
        return "[✓] All advanced settings require various API accesses"
    except Exception as e:
        err = f"[ADVANCED ALL ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_advanced_all():
    try:
        # This is a simplified version - actual advanced settings are complex
        log("[ADVANCED ALL] Attempted to set all advanced settings", Fore.CYAN)
        return "[✓] All advanced settings require various API accesses"
    except Exception as e:
        err = f"[ADVANCED ALL SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_hidden_advanced():
    try:
        # This is a simplified version - actual hidden advanced settings require admin rights
        log("[HIDDEN ADVANCED] Attempted to retrieve hidden advanced settings", Fore.CYAN)
        return "[✓] Hidden advanced settings require admin rights"
    except Exception as e:
        err = f"[HIDDEN ADVANCED ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_hidden_advanced():
    try:
        # This is a simplified version - actual hidden advanced setting requires admin rights
        log("[HIDDEN ADVANCED] Attempted to set hidden advanced settings", Fore.CYAN)
        return "[✓] Hidden advanced settings require admin rights"
    except Exception as e:
        err = f"[HIDDEN ADVANCED SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_registry_hidden():
    try:
        # This is a simplified version - actual hidden registry settings require admin rights
        log("[REGISTRY HIDDEN] Attempted to retrieve hidden registry settings", Fore.CYAN)
        return "[✓] Hidden registry settings require admin rights"
    except Exception as e:
        err = f"[REGISTRY HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_registry_hidden():
    try:
        # This is a simplified version - actual hidden registry setting requires admin rights
        log("[REGISTRY HIDDEN] Attempted to set hidden registry settings", Fore.CYAN)
        return "[✓] Hidden registry settings require admin rights"
    except Exception as e:
        err = f"[REGISTRY HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_performance_hidden():
    try:
        # This is a simplified version - actual hidden performance settings require admin rights
        log("[PERFORMANCE HIDDEN] Attempted to retrieve hidden performance settings", Fore.CYAN)
        return "[✓] Hidden performance settings require admin rights"
    except Exception as e:
        err = f"[PERFORMANCE HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_performance_hidden():
    try:
        # This is a simplified version - actual hidden performance setting requires admin rights
        log("[PERFORMANCE HIDDEN] Attempted to set hidden performance settings", Fore.CYAN)
        return "[✓] Hidden performance settings require admin rights"
    except Exception as e:
        err = f"[PERFORMANCE HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_network_hidden():
    try:
        # This is a simplified version - actual hidden network settings require admin rights
        log("[NETWORK HIDDEN] Attempted to retrieve hidden network settings", Fore.CYAN)
        return "[✓] Hidden network settings require admin rights"
    except Exception as e:
        err = f"[NETWORK HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_network_hidden():
    try:
        # This is a simplified version - actual hidden network setting requires admin rights
        log("[NETWORK HIDDEN] Attempted to set hidden network settings", Fore.CYAN)
        return "[✓] Hidden network settings require admin rights"
    except Exception as e:
        err = f"[NETWORK HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_security_hidden():
    try:
        # This is a simplified version - actual hidden security settings require admin rights
        log("[SECURITY HIDDEN] Attempted to retrieve hidden security settings", Fore.CYAN)
        return "[✓] Hidden security settings require admin rights"
    except Exception as e:
        err = f"[SECURITY HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_security_hidden():
    try:
        # This is a simplified version - actual hidden security setting requires admin rights
        log("[SECURITY HIDDEN] Attempted to set hidden security settings", Fore.CYAN)
        return "[✓] Hidden security settings require admin rights"
    except Exception as e:
        err = f"[SECURITY HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_privacy_hidden():
    try:
        # This is a simplified version - actual hidden privacy settings require admin rights
        log("[PRIVACY HIDDEN] Attempted to retrieve hidden privacy settings", Fore.CYAN)
        return "[✓] Hidden privacy settings require admin rights"
    except Exception as e:
        err = f"[PRIVACY HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_privacy_hidden():
    try:
        # This is a simplified version - actual hidden privacy setting requires admin rights
        log("[PRIVACY HIDDEN] Attempted to set hidden privacy settings", Fore.CYAN)
        return "[✓] Hidden privacy settings require admin rights"
    except Exception as e:
        err = f"[PRIVACY HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_updates_hidden():
    try:
        # This is a simplified version - actual hidden update settings require admin rights
        log("[UPDATES HIDDEN] Attempted to retrieve hidden update settings", Fore.CYAN)
        return "[✓] Hidden update settings require admin rights"
    except Exception as e:
        err = f"[UPDATES HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_updates_hidden():
    try:
        # This is a simplified version - actual hidden update setting requires admin rights
        log("[UPDATES HIDDEN] Attempted to set hidden update settings", Fore.CYAN)
        return "[✓] Hidden update settings require admin rights"
    except Exception as e:
        err = f"[UPDATES HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_backup_hidden():
    try:
        # This is a simplified version - actual hidden backup settings require admin rights
        log("[BACKUP HIDDEN] Attempted to retrieve hidden backup settings", Fore.CYAN)
        return "[✓] Hidden backup settings require admin rights"
    except Exception as e:
        err = f"[BACKUP HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_backup_hidden():
    try:
        # This is a simplified version - actual hidden backup setting requires admin rights
        log("[BACKUP HIDDEN] Attempted to set hidden backup settings", Fore.CYAN)
        return "[✓] Hidden backup settings require admin rights"
    except Exception as e:
        err = f"[BACKUP HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_display_hidden():
    try:
        # This is a simplified version - actual hidden display settings require admin rights
        log("[DISPLAY HIDDEN] Attempted to retrieve hidden display settings", Fore.CYAN)
        return "[✓] Hidden display settings require admin rights"
    except Exception as e:
        err = f"[DISPLAY HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_display_hidden():
    try:
        # This is a simplified version - actual hidden display setting requires admin rights
        log("[DISPLAY HIDDEN] Attempted to set hidden display settings", Fore.CYAN)
        return "[✓] Hidden display settings require admin rights"
    except Exception as e:
        err = f"[DISPLAY HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_audio_hidden():
    try:
        # This is a simplified version - actual hidden audio settings require admin rights
        log("[AUDIO HIDDEN] Attempted to retrieve hidden audio settings", Fore.CYAN)
        return "[✓] Hidden audio settings require admin rights"
    except Exception as e:
        err = f"[AUDIO HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_audio_hidden():
    try:
        # This is a simplified version - actual hidden audio setting requires admin rights
        log("[AUDIO HIDDEN] Attempted to set hidden audio settings", Fore.CYAN)
        return "[✓] Hidden audio settings require admin rights"
    except Exception as e:
        err = f"[AUDIO HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_power_hidden():
    try:
        # This is a simplified version - actual hidden power settings require admin rights
        log("[POWER HIDDEN] Attempted to retrieve hidden power settings", Fore.CYAN)
        return "[✓] Hidden power settings require admin rights"
    except Exception as e:
        err = f"[POWER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_power_hidden():
    try:
        # This is a simplified version - actual hidden power setting requires admin rights
        log("[POWER HIDDEN] Attempted to set hidden power settings", Fore.CYAN)
        return "[✓] Hidden power settings require admin rights"
    except Exception as e:
        err = f"[POWER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_gpu_hidden():
    try:
        # This is a simplified version - actual hidden GPU settings require admin rights
        log("[GPU HIDDEN] Attempted to retrieve hidden GPU settings", Fore.CYAN)
        return "[✓] Hidden GPU settings require admin rights"
    except Exception as e:
        err = f"[GPU HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_gpu_hidden():
    try:
        # This is a simplified version - actual hidden GPU setting requires admin rights
        log("[GPU HIDDEN] Attempted to set hidden GPU settings", Fore.CYAN)
        return "[✓] Hidden GPU settings require admin rights"
    except Exception as e:
        err = f"[GPU HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_cpu_hidden():
    try:
        # This is a simplified version - actual hidden CPU settings require admin rights
        log("[CPU HIDDEN] Attempted to retrieve hidden CPU settings", Fore.CYAN)
        return "[✓] Hidden CPU settings require admin rights"
    except Exception as e:
        err = f"[CPU HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_cpu_hidden():
    try:
        # This is a simplified version - actual hidden CPU setting requires admin rights
        log("[CPU HIDDEN] Attempted to set hidden CPU settings", Fore.CYAN)
        return "[✓] Hidden CPU settings require admin rights"
    except Exception as e:
        err = f"[CPU HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_memory_hidden():
    try:
        # This is a simplified version - actual hidden memory settings require admin rights
        log("[MEMORY HIDDEN] Attempted to retrieve hidden memory settings", Fore.CYAN)
        return "[✓] Hidden memory settings require admin rights"
    except Exception as e:
        err = f"[MEMORY HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_memory_hidden():
    try:
        # This is a simplified version - actual hidden memory setting requires admin rights
        log("[MEMORY HIDDEN] Attempted to set hidden memory settings", Fore.CYAN)
        return "[✓] Hidden memory settings require admin rights"
    except Exception as e:
        err = f"[MEMORY HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_storage_hidden():
    try:
        # This is a simplified version - actual hidden storage settings require admin rights
        log("[STORAGE HIDDEN] Attempted to retrieve hidden storage settings", Fore.CYAN)
        return "[✓] Hidden storage settings require admin rights"
    except Exception as e:
        err = f"[STORAGE HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_storage_hidden():
    try:
        # This is a simplified version - actual hidden storage setting requires admin rights
        log("[STORAGE HIDDEN] Attempted to set hidden storage settings", Fore.CYAN)
        return "[✓] Hidden storage settings require admin rights"
    except Exception as e:
        err = f"[STORAGE HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_network_card_hidden():
    try:
        # This is a simplified version - actual hidden network card settings require admin rights
        log("[NETWORK CARD HIDDEN] Attempted to retrieve hidden network card settings", Fore.CYAN)
        return "[✓] Hidden network card settings require admin rights"
    except Exception as e:
        err = f"[NETWORK CARD HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_network_card_hidden():
    try:
        # This is a simplified version - actual hidden network card setting requires admin rights
        log("[NETWORK CARD HIDDEN] Attempted to set hidden network card settings", Fore.CYAN)
        return "[✓] Hidden network card settings require admin rights"
    except Exception as e:
        err = f"[NETWORK CARD HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_wifi_card_hidden():
    try:
        # This is a simplified version - actual hidden WiFi card settings require admin rights
        log("[WIFI CARD HIDDEN] Attempted to retrieve hidden WiFi card settings", Fore.CYAN)
        return "[✓] Hidden WiFi card settings require admin rights"
    except Exception as e:
        err = f"[WIFI CARD HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_wifi_card_hidden():
    try:
        # This is a simplified version - actual hidden WiFi card setting requires admin rights
        log("[WIFI CARD HIDDEN] Attempted to set hidden WiFi card settings", Fore.CYAN)
        return "[✓] Hidden WiFi card settings require admin rights"
    except Exception as e:
        err = f"[WIFI CARD HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_bluetooth_card_hidden():
    try:
        # This is a simplified version - actual hidden Bluetooth card settings require admin rights
        log("[BLUETOOTH CARD HIDDEN] Attempted to retrieve hidden Bluetooth card settings", Fore.CYAN)
        return "[✓] Hidden Bluetooth card settings require admin rights"
    except Exception as e:
        err = f"[BLUETOOTH CARD HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_bluetooth_card_hidden():
    try:
        # This is a simplified version - actual hidden Bluetooth card setting requires admin rights
        log("[BLUETOOTH CARD HIDDEN] Attempted to set hidden Bluetooth card settings", Fore.CYAN)
        return "[✓] Hidden Bluetooth card settings require admin rights"
    except Exception as e:
        err = f"[BLUETOOTH CARD HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_usb_controller_hidden():
    try:
        # This is a simplified version - actual hidden USB controller settings require admin rights
        log("[USB CONTROLLER HIDDEN] Attempted to retrieve hidden USB controller settings", Fore.CYAN)
        return "[✓] Hidden USB controller settings require admin rights"
    except Exception as e:
        err = f"[USB CONTROLLER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_usb_controller_hidden():
    try:
        # This is a simplified version - actual hidden USB controller setting requires admin rights
        log("[USB CONTROLLER HIDDEN] Attempted to set hidden USB controller settings", Fore.CYAN)
        return "[✓] Hidden USB controller settings require admin rights"
    except Exception as e:
        err = f"[USB CONTROLLER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_audio_controller_hidden():
    try:
        # This is a simplified version - actual hidden audio controller settings require admin rights
        log("[AUDIO CONTROLLER HIDDEN] Attempted to retrieve hidden audio controller settings", Fore.CYAN)
        return "[✓] Hidden audio controller settings require admin rights"
    except Exception as e:
        err = f"[AUDIO CONTROLLER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_audio_controller_hidden():
    try:
        # This is a simplified version - actual hidden audio controller setting requires admin rights
        log("[AUDIO CONTROLLER HIDDEN] Attempted to set hidden audio controller settings", Fore.CYAN)
        return "[✓] Hidden audio controller settings require admin rights"
    except Exception as e:
        err = f"[AUDIO CONTROLLER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_video_controller_hidden():
    try:
        # This is a simplified version - actual hidden video controller settings require admin rights
        log("[VIDEO CONTROLLER HIDDEN] Attempted to retrieve hidden video controller settings", Fore.CYAN)
        return "[✓] Hidden video controller settings require admin rights"
    except Exception as e:
        err = f"[VIDEO CONTROLLER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_video_controller_hidden():
    try:
        # This is a simplified version - actual hidden video controller setting requires admin rights
        log("[VIDEO CONTROLLER HIDDEN] Attempted to set hidden video controller settings", Fore.CYAN)
        return "[✓] Hidden video controller settings require admin rights"
    except Exception as e:
        err = f"[VIDEO CONTROLLER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_printer_hidden():
    try:
        # This is a simplified version - actual hidden printer settings require admin rights
        log("[PRINTER HIDDEN] Attempted to retrieve hidden printer settings", Fore.CYAN)
        return "[✓] Hidden printer settings require admin rights"
    except Exception as e:
        err = f"[PRINTER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_printer_hidden():
    try:
        # This is a simplified version - actual hidden printer setting requires admin rights
        log("[PRINTER HIDDEN] Attempted to set hidden printer settings", Fore.CYAN)
        return "[✓] Hidden printer settings require admin rights"
    except Exception as e:
        err = f"[PRINTER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_camera_hidden():
    try:
        # This is a simplified version - actual hidden camera settings require admin rights
        log("[CAMERA HIDDEN] Attempted to retrieve hidden camera settings", Fore.CYAN)
        return "[✓] Hidden camera settings require admin rights"
    except Exception as e:
        err = f"[CAMERA HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_camera_hidden():
    try:
        # This is a simplified version - actual hidden camera setting requires admin rights
        log("[CAMERA HIDDEN] Attempted to set hidden camera settings", Fore.CYAN)
        return "[✓] Hidden camera settings require admin rights"
    except Exception as e:
        err = f"[CAMERA HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_microphone_hidden():
    try:
        # This is a simplified version - actual hidden microphone settings require admin rights
        log("[MICROPHONE HIDDEN] Attempted to retrieve hidden microphone settings", Fore.CYAN)
        return "[✓] Hidden microphone settings require admin rights"
    except Exception as e:
        err = f"[MICROPHONE HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_microphone_hidden():
    try:
        # This is a simplified version - actual hidden microphone setting requires admin rights
        log("[MICROPHONE HIDDEN] Attempted to set hidden microphone settings", Fore.CYAN)
        return "[✓] Hidden microphone settings require admin rights"
    except Exception as e:
        err = f"[MICROPHONE HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_speaker_hidden():
    try:
        # This is a simplified version - actual hidden speaker settings require admin rights
        log("[SPEAKER HIDDEN] Attempted to retrieve hidden speaker settings", Fore.CYAN)
        return "[✓] Hidden speaker settings require admin rights"
    except Exception as e:
        err = f"[SPEAKER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_speaker_hidden():
    try:
        # This is a simplified version - actual hidden speaker setting requires admin rights
        log("[SPEAKER HIDDEN] Attempted to set hidden speaker settings", Fore.CYAN)
        return "[✓] Hidden speaker settings require admin rights"
    except Exception as e:
        err = f"[SPEAKER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_game_hidden():
    try:
        # This is a simplified version - actual hidden game settings require admin rights
        log("[GAME HIDDEN] Attempted to retrieve hidden game settings", Fore.CYAN)
        return "[✓] Hidden game settings require admin rights"
    except Exception as e:
        err = f"[GAME HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_game_hidden():
    try:
        # This is a simplified version - actual hidden game setting requires admin rights
        log("[GAME HIDDEN] Attempted to set hidden game settings", Fore.CYAN)
        return "[✓] Hidden game settings require admin rights"
    except Exception as e:
        err = f"[GAME HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_developer_hidden():
    try:
        # This is a simplified version - actual hidden developer settings require admin rights
        log("[DEVELOPER HIDDEN] Attempted to retrieve hidden developer settings", Fore.CYAN)
        return "[✓] Hidden developer settings require admin rights"
    except Exception as e:
        err = f"[DEVELOPER HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_developer_hidden():
    try:
        # This is a simplified version - actual hidden developer setting requires admin rights
        log("[DEVELOPER HIDDEN] Attempted to set hidden developer settings", Fore.CYAN)
        return "[✓] Hidden developer settings require admin rights"
    except Exception as e:
        err = f"[DEVELOPER HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_admin_hidden():
    try:
        # This is a simplified version - actual hidden admin settings require admin rights
        log("[ADMIN HIDDEN] Attempted to retrieve hidden admin settings", Fore.CYAN)
        return "[✓] Hidden admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_admin_hidden():
    try:
        # This is a simplified version - actual hidden admin setting requires admin rights
        log("[ADMIN HIDDEN] Attempted to set hidden admin settings", Fore.CYAN)
        return "[✓] Hidden admin settings require admin rights"
    except Exception as e:
        err = f"[ADMIN HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def get_system_all_hidden():
    try:
        # This is a simplified version - actual all hidden settings require admin rights
        log("[ALL HIDDEN] Attempted to retrieve all hidden settings", Fore.CYAN)
        return "[✓] All hidden settings require admin rights"
    except Exception as e:
        err = f"[ALL HIDDEN ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

def set_system_all_hidden():
    try:
        # This is a simplified version - actual all hidden setting requires admin rights
        log("[ALL HIDDEN] Attempted to set all hidden settings", Fore.CYAN)
        return "[✓] All hidden settings require admin rights"
    except Exception as e:
        err = f"[ALL HIDDEN SET ERROR] {str(e)}"
        log(err, Fore.RED)
        return err

# === AI RESPONSE FUNCTION (Advanced multi-step tasks) ===
def get_advanced_response(user_input):
    global history
    
    # Build context for advanced AI with human-like control
    context = (
        "You are an ULTIMATE HUMANITY AI assistant with full computer control capabilities. "
        "You understand complex natural language and can execute sophisticated multi-step tasks. "
        "You have access to these advanced tools:\n"
        "- open_note: Open a new note in Windows (params: none)\n"
        "- write_note: Write content to active note (params: content)\n"
        "- save_note: Save the current note (params: none)\n"
        "- copy_text: Copy text to clipboard (params: text)\n"
        "- paste_text: Paste text from clipboard (params: none)\n"
        "- smart_copy_paste: Write content to note, copy it (params: content)\n"
        "- find_and_open_pages: Find and open multiple web pages (params: query, num_pages)\n"
        "- write_creative_story: Write and save a creative story (params: topic)\n"
        "- analyze_web_content: Analyze web page content (params: url)\n"
        "- sign_in_to_website: Attempt to sign in to website (params: url, username, password)\n"
        "- chat_with_ai: Chat with AI assistant (params: message)\n"
        "- search: Search Google for information (params: query)\n"
        "- browse: Open websites (params: url)\n"
        "- cmd: Execute Windows commands (params: command)\n"
        "- read: Read file content (params: file_path)\n"
        "- write: Write to file (params: file_path, content)\n"
        "- mouse: Control mouse (params: x, y, action)\n"
        "- type: Type text (params: text)\n"
        "- screenshot: Take screenshot (params: none)\n"
        "- extract: Extract current page content (params: none)\n"
        "- download: Download files (params: url, filename)\n"
        "- click_element: Click web element (params: selector, selector_type)\n"
        "- fill_form_field: Fill form field (params: selector, value, selector_type)\n"
        "- scroll_mouse: Scroll mouse wheel (params: clicks)\n"
        "- drag_mouse: Drag mouse (params: x1, y1, x2, y2, duration)\n"
        "- press_key: Press a key (params: key)\n"
        "- press_hotkey: Press key combination (params: keys)\n"
        "- focus_window: Focus on window (params: title)\n"
        "- minimize_window: Minimize window (params: title)\n"
        "- maximize_window: Maximize window (params: title)\n"
        "- close_window: Close window (params: title)\n"
        "- get_system_info: Get system information (params: none)\n"
        "- run_powershell_command: Run PowerShell command (params: command)\n"
        "- list_processes: List running processes (params: none)\n"
        "- kill_process_by_name: Kill process by name (params: name)\n"
        "- get_window_list: Get list of windows (params: none)\n"
        "- send_text_to_window: Send text to window (params: window_title, text)\n"
        "- take_full_screenshot: Take full screen screenshot (params: none)\n"
        "- record_screen: Record screen (params: duration)\n"
        "- get_mouse_position: Get current mouse position (params: none)\n"
        "- get_active_window: Get active window title (params: none)\n"
        "- get_clipboard_content: Get clipboard content (params: none)\n"
        "- clear_clipboard: Clear clipboard (params: none)\n"
        "- get_all_files_in_directory: Get files in directory (params: directory, pattern)\n"
        "- create_directory: Create directory (params: path)\n"
        "- delete_file: Delete file (params: path)\n"
        "- delete_directory: Delete directory (params: path)\n"
        "- zip_directory: Zip directory (params: source_dir, zip_path)\n"
        "- unzip_file: Unzip file (params: zip_path, extract_to)\n"
        "- get_network_info: Get network information (params: none)\n"
        "- ping_host: Ping host (params: host)\n"
        "- get_wifi_networks: Get available WiFi networks (params: none)\n"
        "- connect_to_wifi: Connect to WiFi (params: ssid, password)\n"
        "- get_battery_status: Get battery status (params: none)\n"
        "- shutdown_computer: Shutdown computer (params: delay)\n"
        "- restart_computer: Restart computer (params: delay)\n"
        "- sleep_computer: Sleep computer (params: none)\n"
        "- lock_computer: Lock computer (params: none)\n"
        "- get_installed_programs: Get installed programs (params: none)\n"
        "- get_running_services: Get running services (params: none)\n"
        "- start_service: Start service (params: service_name)\n"
        "- stop_service: Stop service (params: service_name)\n"
        "- get_registry_value: Get registry value (params: hive, key_path, value_name)\n"
        "- set_registry_value: Set registry value (params: hive, key_path, value_name, value)\n"
        "- get_cpu_info: Get CPU information (params: none)\n"
        "- get_memory_info: Get memory information (params: none)\n"
        "- get_disk_info: Get disk information (params: none)\n"
        "- get_network_stats: Get network statistics (params: none)\n"
        "- get_system_uptime: Get system uptime (params: none)\n"
        "- get_user_accounts: Get user accounts (params: none)\n"
        "- create_user_account: Create user account (params: username, password)\n"
        "- delete_user_account: Delete user account (params: username)\n"
        "- get_startup_programs: Get startup programs (params: none)\n"
        "- add_to_startup: Add to startup (params: name, path)\n"
        "- remove_from_startup: Remove from startup (params: name)\n"
        "- get_recent_files: Get recent files (params: none)\n"
        "- get_recent_documents: Get recent documents (params: none)\n"
        "- get_browser_history: Get browser history (params: none)\n"
        "- get_installed_apps: Get installed apps (params: none)\n"
        "- get_system_drivers: Get system drivers (params: none)\n"
        "- update_driver: Update driver (params: driver_name)\n"
        "- get_windows_updates: Get Windows updates (params: none)\n"
        "- install_windows_updates: Install Windows updates (params: none)\n"
        "- get_antivirus_status: Get antivirus status (params: none)\n"
        "- get_firewall_status: Get firewall status (params: none)\n"
        "- enable_firewall: Enable firewall (params: none)\n"
        "- disable_firewall: Disable firewall (params: none)\n"
        "- get_system_performance: Get system performance (params: none)\n"
        "- optimize_system: Optimize system (params: none)\n"
        "- get_hardware_info: Get hardware information (params: none)\n"
        "- get_software_info: Get software information (params: none)\n"
        "- get_system_logs: Get system logs (params: none)\n"
        "- clear_system_logs: Clear system logs (params: none)\n"
        "- get_temp_files: Get temporary files (params: none)\n"
        "- clear_temp_files: Clear temporary files (params: none)\n"
        "- get_recycle_bin_contents: Get recycle bin contents (params: none)\n"
        "- empty_recycle_bin: Empty recycle bin (params: none)\n"
        "- get_disk_space_info: Get disk space information (params: none)\n"
        "- get_network_connections: Get network connections (params: none)\n"
        "- get_processes_by_cpu_usage: Get processes by CPU usage (params: none)\n"
        "- get_processes_by_memory_usage: Get processes by memory usage (params: none)\n"
        "- get_system_environment: Get system environment (params: none)\n"
        "- get_system_time: Get system time (params: none)\n"
        "- set_system_time: Set system time (params: new_time)\n"
        "- get_timezone_info: Get timezone information (params: none)\n"
        "- get_system_locale: Get system locale (params: none)\n"
        "- get_system_language: Get system language (params: none)\n"
        "- get_system_fonts: Get system fonts (params: none)\n"
        "- get_system_themes: Get system themes (params: none)\n"
        "- get_system_wallpaper: Get system wallpaper (params: none)\n"
        "- set_system_wallpaper: Set system wallpaper (params: image_path)\n"
        "- get_screen_resolution: Get screen resolution (params: none)\n"
        "- set_screen_resolution: Set screen resolution (params: width, height)\n"
        "- get_screen_color_depth: Get screen color depth (params: none)\n"
        "- get_screen_refresh_rate: Get screen refresh rate (params: none)\n"
        "- get_audio_devices: Get audio devices (params: none)\n"
        "- get_microphone_status: Get microphone status (params: none)\n"
        "- get_speakers_status: Get speakers status (params: none)\n"
        "- get_volume_level: Get volume level (params: none)\n"
        "- set_volume_level: Set volume level (params: level)\n"
        "- mute_audio: Mute audio (params: none)\n"
        "- unmute_audio: Unmute audio (params: none)\n"
        "- record_audio: Record audio (params: duration)\n"
        "- play_audio: Play audio file (params: file_path)\n"
        "- get_camera_status: Get camera status (params: none)\n"
        "- take_camera_photo: Take camera photo (params: none)\n"
        "- start_camera_recording: Start camera recording (params: none)\n"
        "- stop_camera_recording: Stop camera recording (params: none)\n"
        "- get_bluetooth_status: Get Bluetooth status (params: none)\n"
        "- get_connected_bluetooth_devices: Get connected Bluetooth devices (params: none)\n"
        "- connect_bluetooth_device: Connect Bluetooth device (params: device_address)\n"
        "- disconnect_bluetooth_device: Disconnect Bluetooth device (params: device_address)\n"
        "- get_usb_devices: Get connected USB devices (params: none)\n"
        "- get_serial_ports: Get serial ports (params: none)\n"
        "- get_parallel_ports: Get parallel ports (params: none)\n"
        "- get_system_sensors: Get system sensors (params: none)\n"
        "- get_gpu_info: Get GPU information (params: none)\n"
        "- get_system_temperatures: Get system temperatures (params: none)\n"
        "- get_system_fans: Get system fans (params: none)\n"
        "- get_system_power_status: Get system power status (params: none)\n"
        "- get_system_updates_info: Get system updates info (params: none)\n"
        "- get_system_backup_status: Get system backup status (params: none)\n"
        "- create_system_backup: Create system backup (params: none)\n"
        "- restore_system_backup: Restore system backup (params: none)\n"
        "- get_system_restore_points: Get system restore points (params: none)\n"
        "- create_system_restore_point: Create system restore point (params: description)\n"
        "- restore_system_to_point: Restore system to point (params: point_id)\n"
        "- get_system_performance_counters: Get performance counters (params: none)\n"
        "- get_system_event_logs: Get event logs (params: none)\n"
        "- clear_system_event_logs: Clear event logs (params: none)\n"
        "- get_system_registry_info: Get registry info (params: none)\n"
        "- backup_system_registry: Backup registry (params: none)\n"
        "- restore_system_registry: Restore registry (params: backup_path)\n"
        "- get_system_service_status: Get service status (params: service_name)\n"
        "- get_system_startup_items: Get startup items (params: none)\n"
        "- add_system_startup_item: Add startup item (params: name, path)\n"
        "- remove_system_startup_item: Remove startup item (params: name)\n"
        "- get_system_environment_variables: Get environment variables (params: none)\n"
        "- set_system_environment_variable: Set environment variable (params: name, value)\n"
        "- delete_system_environment_variable: Delete environment variable (params: name)\n"
        "- get_system_timezone: Get system timezone (params: none)\n"
        "- set_system_timezone: Set system timezone (params: timezone_name)\n"
        "- get_system_locale_settings: Get locale settings (params: none)\n"
        "- set_system_locale: Set system locale (params: locale_name)\n"
        "- get_system_language_settings: Get language settings (params: none)\n"
        "- set_system_language: Set system language (params: language_code)\n"
        "- get_system_keyboard_layout: Get keyboard layout (params: none)\n"
        "- set_system_keyboard_layout: Set keyboard layout (params: layout_code)\n"
        "- get_system_mouse_settings: Get mouse settings (params: none)\n"
        "- set_system_mouse_settings: Set mouse settings (params: speed, acceleration)\n"
        "- get_system_display_settings: Get display settings (params: none)\n"
        "- set_system_display_settings: Set display settings (params: brightness, contrast)\n"
        "- get_system_audio_settings: Get audio settings (params: none)\n"
        "- set_system_audio_settings: Set audio settings (params: volume, mute)\n"
        "- get_system_power_settings: Get power settings (params: none)\n"
        "- set_system_power_settings: Set power settings (params: scheme, timeout)\n"
        "- get_system_security_settings: Get security settings (params: none)\n"
        "- set_system_security_settings: Set security settings (params: enhanced_security)\n"
        "- get_system_privacy_settings: Get privacy settings (params: none)\n"
        "- set_system_privacy_settings: Set privacy settings (params: data_collection, location_tracking)\n"
        "- get_system_updates_settings: Get updates settings (params: none)\n"
        "- set_system_updates_settings: Set updates settings (params: auto_updates, download_only)\n"
        "- get_system_backup_settings: Get backup settings (params: none)\n"
        "- set_system_backup_settings: Set backup settings (params: auto_backup, backup_location)\n"
        "- get_system_network_settings: Get network settings (params: none)\n"
        "- set_system_network_settings: Set network settings (params: proxy_server, dns_server)\n"
        "- get_system_wifi_settings: Get WiFi settings (params: none)\n"
        "- set_system_wifi_settings: Set WiFi settings (params: ssid, password, auto_connect)\n"
        "- get_system_bluetooth_settings: Get Bluetooth settings (params: none)\n"
        "- set_system_bluetooth_settings: Set Bluetooth settings (params: enabled, discoverable)\n"
        "- get_system_usb_settings: Get USB settings (params: none)\n"
        "- set_system_usb_settings: Set USB settings (params: auto_install_drivers, power_saving)\n"
        "- get_system_printer_settings: Get printer settings (params: none)\n"
        "- set_system_printer_settings: Set printer settings (params: default_printer, print_quality)\n"
        "- get_system_camera_settings: Get camera settings (params: none)\n"
        "- set_system_camera_settings: Set camera settings (params: resolution, frame_rate)\n"
        "- get_system_microphone_settings: Get microphone settings (params: none)\n"
        "- set_system_microphone_settings: Set microphone settings (params: sensitivity, noise_reduction)\n"
        "- get_system_speaker_settings: Get speaker settings (params: none)\n"
        "- set_system_speaker_settings: Set speaker settings (params: volume, bass, treble)\n"
        "- get_system_game_settings: Get game settings (params: none)\n"
        "- set_system_game_settings: Set game settings (params: high_performance, vsync)\n"
        "- get_system_developer_settings: Get developer settings (params: none)\n"
        "- set_system_developer_settings: Set developer settings (params: developer_mode, usb_debugging)\n"
        "- get_system_admin_settings: Get admin settings (params: none)\n"
        "- set_system_admin_settings: Set admin settings (params: admin_password)\n"
        "- get_system_advanced_settings: Get advanced settings (params: none)\n"
        "- set_system_advanced_settings: Set advanced settings (params: advanced_features)\n"
        "- get_system_hidden_settings: Get hidden settings (params: none)\n"
        "- set_system_hidden_settings: Set hidden settings (params: enable_hidden)\n"
        "- get_system_registry_advanced: Get advanced registry settings (params: none)\n"
        "- set_system_registry_advanced: Set advanced registry setting (params: key_path, value_name, value_data)\n"
        "- get_system_performance_advanced: Get advanced performance settings (params: none)\n"
        "- set_system_performance_advanced: Set advanced performance settings (params: ram_boost, cpu_priority)\n"
        "- get_system_network_advanced: Get advanced network settings (params: none)\n"
        "- set_system_network_advanced: Set advanced network settings (params: buffer_size, connection_timeout)\n"
        "- get_system_security_advanced: Get advanced security settings (params: none)\n"
        "- set_system_security_advanced: Set advanced security settings (params: real_time_protection, firewall_level)\n"
        "- get_system_privacy_advanced: Get advanced privacy settings (params: none)\n"
        "- set_system_privacy_advanced: Set advanced privacy settings (params: app_tracking, diagnostic_data)\n"
        "- get_system_updates_advanced: Get advanced updates settings (params: none)\n"
        "- set_system_updates_advanced: Set advanced updates settings (params: auto_download, schedule_time)\n"
        "- get_system_backup_advanced: Get advanced backup settings (params: none)\n"
        "- set_system_backup_advanced: Set advanced backup settings (params: backup_frequency, retention_days)\n"
        "- get_system_display_advanced: Get advanced display settings (params: none)\n"
        "- set_system_display_advanced: Set advanced display settings (params: color_temperature, refresh_rate)\n"
        "- get_system_audio_advanced: Get advanced audio settings (params: none)\n"
        "- set_system_audio_advanced: Set advanced audio settings (params: sample_rate, bit_depth)\n"
        "- get_system_power_advanced: Get advanced power settings (params: none)\n"
        "- set_system_power_advanced: Set advanced power settings (params: cpu_governor, gpu_boost)\n"
        "- get_system_gpu_advanced: Get advanced GPU settings (params: none)\n"
        "- set_system_gpu_advanced: Set advanced GPU settings (params: overclock_gpu, memory_clock)\n"
        "- get_system_cpu_advanced: Get advanced CPU settings (params: none)\n"
        "- set_system_cpu_advanced: Set advanced CPU settings (params: overclock_cpu, voltage)\n"
        "- get_system_memory_advanced: Get advanced memory settings (params: none)\n"
        "- set_system_memory_advanced: Set advanced memory settings (params: timing, voltage)\n"
        "- get_system_storage_advanced: Get advanced storage settings (params: none)\n"
        "- set_system_storage_advanced: Set advanced storage settings (params: trim_enabled, cache_size)\n"
        "- get_system_network_card_advanced: Get advanced network card settings (params: none)\n"
        "- set_system_network_card_advanced: Set advanced network card settings (params: speed, duplex)\n"
        "- get_system_wifi_card_advanced: Get advanced WiFi card settings (params: none)\n"
        "- set_system_wifi_card_advanced: Set advanced WiFi card settings (params: channel, power)\n"
        "- get_system_bluetooth_card_advanced: Get advanced Bluetooth card settings (params: none)\n"
        "- set_system_bluetooth_card_advanced: Set advanced Bluetooth card settings (params: power_level, connection_timeout)\n"
        "- get_system_usb_controller_advanced: Get advanced USB controller settings (params: none)\n"
        "- set_system_usb_controller_advanced: Set advanced USB controller settings (params: power_management, bandwidth_limit)\n"
        "- get_system_audio_controller_advanced: Get advanced audio controller settings (params: none)\n"
        "- set_system_audio_controller_advanced: Set advanced audio controller settings (params: sample_rate, buffer_size)\n"
        "- get_system_video_controller_advanced: Get advanced video controller settings (params: none)\n"
        "- set_system_video_controller_advanced: Set advanced video controller settings (params: color_depth, refresh_rate)\n"
        "- get_system_printer_advanced: Get advanced printer settings (params: none)\n"
        "- set_system_printer_advanced: Set advanced printer settings (params: dpi, paper_size)\n"
        "- get_system_camera_advanced: Get advanced camera settings (params: none)\n"
        "- set_system_camera_advanced: Set advanced camera settings (params: exposure, iso)\n"
        "- get_system_microphone_advanced: Get advanced microphone settings (params: none)\n"
        "- set_system_microphone_advanced: Set advanced microphone settings (params: gain, sample_rate)\n"
        "- get_system_speaker_advanced: Get advanced speaker settings (params: none)\n"
        "- set_system_speaker_advanced: Set advanced speaker settings (params: crossover_frequency, bass_management)\n"
        "- get_system_game_advanced: Get advanced game settings (params: none)\n"
        "- set_system_game_advanced: Set advanced game settings (params: frame_limit, texture_quality)\n"
        "- get_system_developer_advanced: Get advanced developer settings (params: none)\n"
        "- set_system_developer_advanced: Set advanced developer settings (params: debug_mode, performance_profiling)\n"
        "- get_system_admin_advanced: Get advanced admin settings (params: none)\n"
        "- set_system_admin_advanced: Set advanced admin settings (params: enable_remote_access, audit_log_level)\n"
        "- get_system_advanced_all: Get all advanced settings (params: none)\n"
        "- set_system_advanced_all: Set all advanced settings (params: none)\n"
        "- get_system_hidden_advanced: Get hidden advanced settings (params: none)\n"
        "- set_system_hidden_advanced: Set hidden advanced settings (params: none)\n"
        "- get_system_registry_hidden: Get hidden registry settings (params: none)\n"
        "- set_system_registry_hidden: Set hidden registry settings (params: none)\n"
        "- get_system_performance_hidden: Get hidden performance settings (params: none)\n"
        "- set_system_performance_hidden: Set hidden performance settings (params: none)\n"
        "- get_system_network_hidden: Get hidden network settings (params: none)\n"
        "- set_system_network_hidden: Set hidden network settings (params: none)\n"
        "- get_system_security_hidden: Get hidden security settings (params: none)\n"
        "- set_system_security_hidden: Set hidden security settings (params: none)\n"
        "- get_system_privacy_hidden: Get hidden privacy settings (params: none)\n"
        "- set_system_privacy_hidden: Set hidden privacy settings (params: none)\n"
        "- get_system_updates_hidden: Get hidden update settings (params: none)\n"
        "- set_system_updates_hidden: Set hidden update settings (params: none)\n"
        "- get_system_backup_hidden: Get hidden backup settings (params: none)\n"
        "- set_system_backup_hidden: Set hidden backup settings (params: none)\n"
        "- get_system_display_hidden: Get hidden display settings (params: none)\n"
        "- set_system_display_hidden: Set hidden display settings (params: none)\n"
        "- get_system_audio_hidden: Get hidden audio settings (params: none)\n"
        "- set_system_audio_hidden: Set hidden audio settings (params: none)\n"
        "- get_system_power_hidden: Get hidden power settings (params: none)\n"
        "- set_system_power_hidden: Set hidden power settings (params: none)\n"
        "- get_system_gpu_hidden: Get hidden GPU settings (params: none)\n"
        "- set_system_gpu_hidden: Set hidden GPU settings (params: none)\n"
        "- get_system_cpu_hidden: Get hidden CPU settings (params: none)\n"
        "- set_system_cpu_hidden: Set hidden CPU settings (params: none)\n"
        "- get_system_memory_hidden: Get hidden memory settings (params: none)\n"
        "- set_system_memory_hidden: Set hidden memory settings (params: none)\n"
        "- get_system_storage_hidden: Get hidden storage settings (params: none)\n"
        "- set_system_storage_hidden: Set hidden storage settings (params: none)\n"
        "- get_system_network_card_hidden: Get hidden network card settings (params: none)\n"
        "- set_system_network_card_hidden: Set hidden network card settings (params: none)\n"
        "- get_system_wifi_card_hidden: Get hidden WiFi card settings (params: none)\n"
        "- set_system_wifi_card_hidden: Set hidden WiFi card settings (params: none)\n"
        "- get_system_bluetooth_card_hidden: Get hidden Bluetooth card settings (params: none)\n"
        "- set_system_bluetooth_card_hidden: Set hidden Bluetooth card settings (params: none)\n"
        "- get_system_usb_controller_hidden: Get hidden USB controller settings (params: none)\n"
        "- set_system_usb_controller_hidden: Set hidden USB controller settings (params: none)\n"
        "- get_system_audio_controller_hidden: Get hidden audio controller settings (params: none)\n"
        "- set_system_audio_controller_hidden: Set hidden audio controller settings (params: none)\n"
        "- get_system_video_controller_hidden: Get hidden video controller settings (params: none)\n"
        "- set_system_video_controller_hidden: Set hidden video controller settings (params: none)\n"
        "- get_system_printer_hidden: Get hidden printer settings (params: none)\n"
        "- set_system_printer_hidden: Set hidden printer settings (params: none)\n"
        "- get_system_camera_hidden: Get hidden camera settings (params: none)\n"
        "- set_system_camera_hidden: Set hidden camera settings (params: none)\n"
        "- get_system_microphone_hidden: Get hidden microphone settings (params: none)\n"
        "- set_system_microphone_hidden: Set hidden microphone settings (params: none)\n"
        "- get_system_speaker_hidden: Get hidden speaker settings (params: none)\n"
        "- set_system_speaker_hidden: Set hidden speaker settings (params: none)\n"
        "- get_system_game_hidden: Get hidden game settings (params: none)\n"
        "- set_system_game_hidden: Set hidden game settings (params: none)\n"
        "- get_system_developer_hidden: Get hidden developer settings (params: none)\n"
        "- set_system_developer_hidden: Set hidden developer settings (params: none)\n"
        "- get_system_admin_hidden: Get hidden admin settings (params: none)\n"
        "- set_system_admin_hidden: Set hidden admin settings (params: none)\n"
        "- get_system_all_hidden: Get all hidden settings (params: none)\n"
        "- set_system_all_hidden: Set all hidden settings (params: none)\n"
        "- chat: Respond to user (params: text)\n\n"
        "ADVANCED HUMANITY RULES:\n"
        "1. ALWAYS respond with valid JSON array of actions\n"
        "2. For complex requests, break into multiple steps\n"
        "3. Execute tasks in correct sequence\n"
        "4. Combine multiple tools for complex goals\n"
        "5. Control computer like a human (mouse, keyboard, etc.)\n"
        "6. Generate content when requested (stories, articles, etc.)\n"
        "7. Never return plain text instead of JSON\n"
        "8. Always provide actionable results\n\n"
        "Example response format:\n"
        '[{"tool": "open_note", "params": {}}, {"tool": "write_note", "params": {"content": "Content to write"}}, {"tool": "save_note", "params": {}}]'
    )
    
    messages = [{"role": "user", "content": context}]
    for h in history[-2:]:  # Reduced history for speed
        if isinstance(h, dict) and "user" in h and "ai" in h:
            messages.append({"role": "user", "content": h["user"]})
            messages.append({"role": "assistant", "content": h["ai"]})
    messages.append({"role": "user", "content": user_input})
    
    # Try Gemini first
    try:
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content(
            messages,
            generation_config={
                "temperature": 0.8,
                "max_output_tokens": 1500,
            }
        )
        result = response.text.strip()
        
        # Ensure it's valid JSON
        if not result.startswith('[') and not result.startswith('{'):
            return create_advanced_fallback_response(user_input)
        
        return result
    except Exception as e:
        log(f"[GEMINI ERROR] {str(e)}, trying Qwen...", Fore.YELLOW)
        
        # Fallback to Qwen
        try:
            qwen_response = qwen_client.chat.completions.create(
                model="openchat/openchat-7b:free",
                messages=messages,
                max_tokens=1500,
                temperature=0.8
            )
            result = qwen_response.choices[0].message.content.strip()
            
            # Ensure it's valid JSON
            if not result.startswith('[') and not result.startswith('{'):
                return create_advanced_fallback_response(user_input)
            
            return result
        except Exception as e2:
            log(f"[QWEN ERROR] {str(e2)}, trying GPT-4...", Fore.YELLOW)
            
            # Fallback to GPT-4
            try:
                gpt4_response = gpt4_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=1500,
                    temperature=0.8
                )
                result = gpt4_response.choices[0].message.content.strip()
                
                # Ensure it's valid JSON
                if not result.startswith('[') and not result.startswith('{'):
                    return create_advanced_fallback_response(user_input)
                
                return result
            except Exception as e3:
                log(f"[GPT-4 ERROR] {str(e3)}, using fallback...", Fore.RED)
                return create_advanced_fallback_response(user_input)

def create_advanced_fallback_response(user_input):
    """Create advanced fallback response based on user input"""
    user_lower = user_input.lower()
    
    # Handle note operations
    if any(word in user_lower for word in ["note", "notepad", "new file", "text file"]):
        if any(word in user_lower for word in ["write", "story", "save", "create"]):
            topic = user_input.replace("write", "").replace("story", "").replace("create", "").strip()
            return f'[{{"tool": "write_creative_story", "params": {{"topic": "{topic}"}}}}]'
        else:
            return '[{"tool": "open_note", "params": {}}]'
    
    # Handle web operations
    elif any(word in user_lower for word in ["find", "different", "pages", "open", "browse", "website", "websites"]):
        query = user_input.replace("find me", "").replace("open", "").replace("different", "").replace("pages", "").strip()
        if not query:
            query = "popular websites"
        return f'[{{"tool": "find_and_open_pages", "params": {{"query": "{query}", "num_pages": 5}}}}]'
    
    # Handle analysis operations
    elif any(word in user_lower for word in ["analyze", "analyze website", "website", "content"]):
        import re
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', user_input)
        if urls:
            return f'[{{"tool": "analyze_web_content", "params": {{"url": "{urls[0]}"}}}}]'
        else:
            return f'[{{"tool": "search", "params": {{"query": "{user_input}"}}}}]'
    
    # Handle sign-in operations
    elif any(word in user_lower for word in ["sign in", "login", "log in", "sign up"]):
        return f'[{{"tool": "search", "params": {{"query": "{user_input}"}}}}]'
    
    # Handle chat operations
    elif any(word in user_lower for word in ["chat", "talk", "help", "question"]):
        return f'[{{"tool": "chat_with_ai", "params": {{"message": "{user_input}"}}}}]'
    
    # Handle system operations
    elif any(word in user_lower for word in ["system", "info", "information", "status"]):
        return '[{"tool": "get_system_info", "params": {}}]'
    
    # Handle file operations
    elif any(word in user_lower for word in ["file", "read", "write", "create", "delete"]):
        return f'[{{"tool": "search", "params": {{"query": "{user_input}"}}}}]'
    
    # Handle network operations
    elif any(word in user_lower for word in ["network", "wifi", "internet", "connect"]):
        return f'[{{"tool": "get_network_info", "params": }}}]'
    
    # Handle power operations
    elif any(word in user_lower for word in ["shutdown", "restart", "sleep", "lock"]):
        if "shutdown" in user_lower:
            return '[{"tool": "shutdown_computer", "params": {"delay": 0}}]'
        elif "restart" in user_lower:
            return '[{"tool": "restart_computer", "params": {"delay": 0}}]'
        elif "sleep" in user_lower:
            return '[{"tool": "sleep_computer", "params": {}}]'
        elif "lock" in user_lower:
            return '[{"tool": "lock_computer", "params": {}}]'
    
    # Handle general search
    else:
        return f'[{{"tool": "search", "params": {{"query": "{user_input}"}}}}]'

# === ADVANCED PARSING FUNCTION ===
def parse_advanced_response(response_text):
    """Parse advanced AI response that may contain Markdown JSON format"""
    try:
        # Clean response to ensure it's valid JSON
        if "```json" in response_text:
            start = response_text.find("```json") + 7
            end = response_text.find("```", start)
            json_str = response_text[start:end].strip()
            return json.loads(json_str)
        elif "```" in response_text:
            start = response_text.find("```") + 3
            end = response_text.find("```", start)
            json_str = response_text[start:end].strip()
            return json.loads(json_str)
        else:
            # Direct JSON parsing
            return json.loads(response_text)
    except:
        # If parsing fails, try to extract JSON from the text
        try:
            import re
            # Find JSON-like structure
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        
        # Smart fallback based on original input
        return [{"tool": "search", "params": {"query": "default search"}}]

# === MAIN LOOP ===
def main():
    global history, running, driver
    
    log("\n" + "="*60, Fore.MAGENTA)
    log("🤖 ULTIMATE HUMANITY AI ASSISTANT STARTED", Fore.MAGENTA)
    log("✅ Type ANY complex request in natural language", Fore.MAGENTA)
    log("✅ I will execute sophisticated multi-step tasks", Fore.MAGENTA)
    log("✅ Full computer control like TeamViewer", Fore.MAGENTA)
    log("✅ Mouse, keyboard, web, files, system operations", Fore.MAGENTA)
    log("✅ Triple API support (Gemini, Qwen, GPT-4) with fallbacks", Fore.MAGENTA)
    log("✅ Real-time execution with professional results", Fore.MAGENTA)
    log("✅ I will show every action live", Fore.MAGENTA)
    log("✅ I will pause if login/signup needed", Fore.MAGENTA)
    log("✅ Type 'exit' to quit", Fore.MAGENTA)
    log("="*60 + "\n", Fore.MAGENTA)
    
    while running:
        try:
            user_input = input(f"{Fore.BLUE}You: {Style.RESET_ALL}").strip()
            if not user_input:
                continue
            if user_input.lower() == "exit":
                running = False
                break
            
            # Save to history
            history.append({"user": user_input, "ai": ""})
            
            # Get advanced AI plan
            advanced_response = get_advanced_response(user_input)
            log(f"\n[🧠 ADVANCED PLAN] {advanced_response}", Fore.CYAN)
            
            # Parse and execute actions
            actions = parse_advanced_response(advanced_response)
            if not isinstance(actions, list):
                actions = [actions]
            
            results = []
            for action in actions:
                if not running:
                    break
                tool = action.get("tool")
                params = action.get("params", {})
                
                # Fix: Handle when params is a string instead of object
                if isinstance(params, str):
                    if tool == "browse":
                        params = {"url": params}
                    elif tool == "search":
                        params = {"query": params}
                    elif tool == "cmd":
                        params = {"command": params}
                    elif tool == "find_and_open_pages":
                        params = {"query": params, "num_pages": 5}
                    elif tool == "write_creative_story":
                        params = {"topic": params}
                    elif tool == "analyze_web_content":
                        params = {"url": params}
                    elif tool == "chat_with_ai":
                        params = {"message": params}
                    elif tool == "copy_text":
                        params = {"text": params}
                    elif tool == "smart_copy_paste":
                        params = {"content": params}
                    else:
                        params = {}
                
                result = ""
                
                # Map different tool names to same function
                if tool == "open_note":
                    result = open_new_note()
                elif tool == "write_note":
                    result = write_to_note(params.get("content", "Default content"))
                elif tool == "save_note":
                    result = save_note()
                elif tool == "copy_text":
                    result = copy_to_clipboard(params.get("text", "Default text"))
                elif tool == "paste_text":
                    result = paste_from_clipboard()
                elif tool == "smart_copy_paste":
                    result = smart_copy_paste_task(params.get("content", "Default content"))
                elif tool == "find_and_open_pages":
                    query = params.get("query", "websites")
                    num_pages = params.get("num_pages", 5)
                    result = find_and_open_multiple_pages(query, num_pages)
                elif tool == "write_creative_story":
                    topic = params.get("topic", "creative adventure")
                    result = write_creative_story(topic)
                elif tool == "analyze_web_content":
                    url = params.get("url", "https://www.google.com")
                    result = analyze_web_content(url)
                elif tool == "sign_in_to_website":
                    url = params.get("url", "")
                    username = params.get("username", "")
                    password = params.get("password", "")
                    result = sign_in_to_website(url, username, password)
                elif tool == "chat_with_ai":
                    message = params.get("message", "Hello")
                    result = chat_with_ai(message)
                elif tool in ["browse", "open_website", "visit", "go_to"]:
                    result = browse_url(params.get("url", "https://www.google.com"))
                    if driver:
                        check_for_login_or_captcha()
                elif tool in ["search", "google_search"]:
                    result = search_google(params.get("query", user_input))
                    if driver:
                        check_for_login_or_captcha()
                elif tool == "cmd":
                    result = execute_cmd(params.get("command", ""))
                elif tool == "read":
                    result = read_file(params.get("file_path", ""))
                elif tool == "write":
                    result = write_file(params.get("file_path", ""), params.get("content", ""))
                elif tool == "mouse":
                    x = params.get("x", 0)
                    y = params.get("y", 0)
                    action_type = params.get("action", "move")
                    result = move_mouse(x, y, action_type)
                elif tool == "scroll_mouse":
                    clicks = params.get("clicks", 1)
                    result = scroll_mouse(clicks)
                elif tool == "drag_mouse":
                    x1 = params.get("x1", 0)
                    y1 = params.get("y1", 0)
                    x2 = params.get("x2", 100)
                    y2 = params.get("y2", 100)
                    duration = params.get("duration", 0.5)
                    result = drag_mouse(x1, y1, x2, y2, duration)
                elif tool == "type":
                    result = type_text(params.get("text", ""))
                elif tool == "press_key":
                    key = params.get("key", "enter")
                    result = press_key(key)
                elif tool == "press_hotkey":
                    keys = params.get("keys", ["ctrl", "c"])
                    result = press_hotkey(*keys)
                elif tool == "focus_window":
                    title = params.get("title", "")
                    result = focus_window(title)
                elif tool == "minimize_window":
                    title = params.get("title", "")
                    result = minimize_window(title)
                elif tool == "maximize_window":
                    title = params.get("title", "")
                    result = maximize_window(title)
                elif tool == "close_window":
                    title = params.get("title", "")
                    result = close_window(title)
                elif tool == "screenshot":
                    result = take_screenshot()
                elif tool == "extract":
                    result = extract_page_content()
                elif tool == "download":
                    result = download_file(params.get("url", ""), params.get("filename", "downloaded_file"))
                elif tool == "click_element":
                    selector = params.get("selector", "")
                    selector_type = params.get("selector_type", "css")
                    result = click_element(selector, selector_type)
                elif tool == "fill_form_field":
                    selector = params.get("selector", "")
                    value = params.get("value", "")
                    selector_type = params.get("selector_type", "css")
                    result = fill_form_field(selector, value, selector_type)
                elif tool == "get_system_info":
                    result = get_system_info()
                elif tool == "run_powershell_command":
                    command = params.get("command", "")
                    result = run_powershell_command(command)
                elif tool == "list_processes":
                    result = list_processes()
                elif tool == "kill_process_by_name":
                    name = params.get("name", "")
                    result = kill_process_by_name(name)
                elif tool == "get_window_list":
                    result = get_window_list()
                elif tool == "send_text_to_window":
                    title = params.get("window_title", "")
                    text = params.get("text", "")
                    result = send_text_to_window(title, text)
                elif tool == "take_full_screenshot":
                    result = take_full_screenshot()
                elif tool == "record_screen":
                    duration = params.get("duration", 10)
                    result = record_screen(duration)
                elif tool == "get_mouse_position":
                    result = get_mouse_position()
                elif tool == "get_active_window":
                    result = get_active_window()
                elif tool == "get_clipboard_content":
                    result = get_clipboard_content()
                elif tool == "clear_clipboard":
                    result = clear_clipboard()
                elif tool == "get_all_files_in_directory":
                    directory = params.get("directory", ".")
                    pattern = params.get("pattern", "*")
                    result = get_all_files_in_directory(directory, pattern)
                elif tool == "create_directory":
                    path = params.get("path", "")
                    result = create_directory(path)
                elif tool == "delete_file":
                    path = params.get("path", "")
                    result = delete_file(path)
                elif tool == "delete_directory":
                    path = params.get("path", "")
                    result = delete_directory(path)
                elif tool == "zip_directory":
                    source_dir = params.get("source_dir", "")
                    zip_path = params.get("zip_path", "")
                    result = zip_directory(source_dir, zip_path)
                elif tool == "unzip_file":
                    zip_path = params.get("zip_path", "")
                    extract_to = params.get("extract_to", "")
                    result = unzip_file(zip_path, extract_to)
                elif tool == "get_network_info":
                    result = get_network_info()
                elif tool == "ping_host":
                    host = params.get("host", "google.com")
                    result = ping_host(host)
                elif tool == "get_wifi_networks":
                    result = get_wifi_networks()
                elif tool == "connect_to_wifi":
                    ssid = params.get("ssid", "")
                    password = params.get("password", "")
                    result = connect_to_wifi(ssid, password)
                elif tool == "get_battery_status":
                    result = get_battery_status()
                elif tool == "shutdown_computer":
                    delay = params.get("delay", 0)
                    result = shutdown_computer(delay)
                elif tool == "restart_computer":
                    delay = params.get("delay", 0)
                    result = restart_computer(delay)
                elif tool == "sleep_computer":
                    result = sleep_computer()
                elif tool == "lock_computer":
                    result = lock_computer()
                elif tool == "get_installed_programs":
                    result = get_installed_programs()
                elif tool == "get_running_services":
                    result = get_running_services()
                elif tool == "start_service":
                    service_name = params.get("service_name", "")
                    result = start_service(service_name)
                elif tool == "stop_service":
                    service_name = params.get("service_name", "")
                    result = stop_service(service_name)
                elif tool == "get_registry_value":
                    hive = params.get("hive", "HKEY_LOCAL_MACHINE")
                    key_path = params.get("key_path", "")
                    value_name = params.get("value_name", "")
                    result = get_registry_value(hive, key_path, value_name)
                elif tool == "set_registry_value":
                    hive = params.get("hive", "HKEY_LOCAL_MACHINE")
                    key_path = params.get("key_path", "")
                    value_name = params.get("value_name", "")
                    value = params.get("value", "")
                    result = set_registry_value(hive, key_path, value_name, value)
                elif tool == "get_cpu_info":
                    result = get_cpu_info()
                elif tool == "get_memory_info":
                    result = get_memory_info()
                elif tool == "get_disk_info":
                    result = get_disk_info()
                elif tool == "get_network_stats":
                    result = get_network_stats()
                elif tool == "get_system_uptime":
                    result = get_system_uptime()
                elif tool == "get_user_accounts":
                    result = get_user_accounts()
                elif tool == "create_user_account":
                    username = params.get("username", "")
                    password = params.get("password", "")
                    result = create_user_account(username, password)
                elif tool == "delete_user_account":
                    username = params.get("username", "")
                    result = delete_user_account(username)
                elif tool == "get_startup_programs":
                    result = get_startup_programs()
                elif tool == "add_to_startup":
                    name = params.get("name", "")
                    path = params.get("path", "")
                    result = add_to_startup(name, path)
                elif tool == "remove_from_startup":
                    name = params.get("name", "")
                    result = remove_from_startup(name)
                elif tool == "get_recent_files":
                    result = get_recent_files()
                elif tool == "get_recent_documents":
                    result = get_recent_documents()
                elif tool == "get_browser_history":
                    result = get_browser_history()
                elif tool == "get_installed_apps":
                    result = get_installed_apps()
                elif tool == "get_system_drivers":
                    result = get_system_drivers()
                elif tool == "update_driver":
                    driver_name = params.get("driver_name", "")
                    result = update_driver(driver_name)
                elif tool == "get_windows_updates":
                    result = get_windows_updates()
                elif tool == "install_windows_updates":
                    result = install_windows_updates()
                elif tool == "get_antivirus_status":
                    result = get_antivirus_status()
                elif tool == "get_firewall_status":
                    result = get_firewall_status()
                elif tool == "enable_firewall":
                    result = enable_firewall()
                elif tool == "disable_firewall":
                    result = disable_firewall()
                elif tool == "get_system_performance":
                    result = get_system_performance()
                elif tool == "optimize_system":
                    result = optimize_system()
                elif tool == "get_hardware_info":
                    result = get_hardware_info()
                elif tool == "get_software_info":
                    result = get_software_info()
                elif tool == "get_system_logs":
                    result = get_system_logs()
                elif tool == "clear_system_logs":
                    result = clear_system_logs()
                elif tool == "get_temp_files":
                    result = get_temp_files()
                elif tool == "clear_temp_files":
                    result = clear_temp_files()
                elif tool == "get_recycle_bin_contents":
                    result = get_recycle_bin_contents()
                elif tool == "empty_recycle_bin":
                    result = empty_recycle_bin()
                elif tool == "get_disk_space_info":
                    result = get_disk_space_info()
                elif tool == "get_network_connections":
                    result = get_network_connections()
                elif tool == "get_processes_by_cpu_usage":
                    result = get_processes_by_cpu_usage()
                elif tool == "get_processes_by_memory_usage":
                    result = get_processes_by_memory_usage()
                elif tool == "get_system_environment":
                    result = get_system_environment()
                elif tool == "get_system_time":
                    result = get_system_time()
                elif tool == "set_system_time":
                    new_time = params.get("new_time", "")
                    result = set_system_time(new_time)
                elif tool == "get_timezone_info":
                    result = get_timezone_info()
                elif tool == "get_system_locale":
                    result = get_system_locale()
                elif tool == "get_system_language":
                    result = get_system_language()
                elif tool == "get_system_fonts":
                    result = get_system_fonts()
                elif tool == "get_system_themes":
                    result = get_system_themes()
                elif tool == "get_system_wallpaper":
                    result = get_system_wallpaper()
                elif tool == "set_system_wallpaper":
                    image_path = params.get("image_path", "")
                    result = set_system_wallpaper(image_path)
                elif tool == "get_screen_resolution":
                    result = get_screen_resolution()
                elif tool == "set_screen_resolution":
                    width = params.get("width", 1920)
                    height = params.get("height", 1080)
                    result = set_screen_resolution(width, height)
                elif tool == "get_screen_color_depth":
                    result = get_screen_color_depth()
                elif tool == "get_screen_refresh_rate":
                    result = get_screen_refresh_rate()
                elif tool == "get_audio_devices":
                    result = get_audio_devices()
                elif tool == "get_microphone_status":
                    result = get_microphone_status()
                elif tool == "get_speakers_status":
                    result = get_speakers_status()
                elif tool == "get_volume_level":
                    result = get_volume_level()
                elif tool == "set_volume_level":
                    level = params.get("level", 50)
                    result = set_volume_level(level)
                elif tool == "mute_audio":
                    result = mute_audio()
                elif tool == "unmute_audio":
                    result = unmute_audio()
                elif tool == "record_audio":
                    duration = params.get("duration", 5)
                    result = record_audio(duration)
                elif tool == "play_audio":
                    file_path = params.get("file_path", "")
                    result = play_audio(file_path)
                elif tool == "get_camera_status":
                    result = get_camera_status()
                elif tool == "take_camera_photo":
                    result = take_camera_photo()
                elif tool == "start_camera_recording":
                    result = start_camera_recording()
                elif tool == "stop_camera_recording":
                    result = stop_camera_recording()
                elif tool == "get_bluetooth_status":
                    result = get_bluetooth_status()
                elif tool == "get_connected_bluetooth_devices":
                    result = get_connected_bluetooth_devices()
                elif tool == "connect_bluetooth_device":
                    device_address = params.get("device_address", "")
                    result = connect_bluetooth_device(device_address)
                elif tool == "disconnect_bluetooth_device":
                    device_address = params.get("device_address", "")
                    result = disconnect_bluetooth_device(device_address)
                elif tool == "get_usb_devices":
                    result = get_usb_devices()
                elif tool == "get_serial_ports":
                    result = get_serial_ports()
                elif tool == "get_parallel_ports":
                    result = get_parallel_ports()
                elif tool == "get_system_sensors":
                    result = get_system_sensors()
                elif tool == "get_gpu_info":
                    result = get_gpu_info()
                elif tool == "get_system_temperatures":
                    result = get_system_temperatures()
                elif tool == "get_system_fans":
                    result = get_system_fans()
                elif tool == "get_system_power_status":
                    result = get_system_power_status()
                elif tool == "get_system_updates_info":
                    result = get_system_updates_info()
                elif tool == "get_system_backup_status":
                    result = get_system_backup_status()
                elif tool == "create_system_backup":
                    result = create_system_backup()
                elif tool == "restore_system_backup":
                    result = restore_system_backup()
                elif tool == "get_system_restore_points":
                    result = get_system_restore_points()
                elif tool == "create_system_restore_point":
                    description = params.get("description", "Manual Restore Point")
                    result = create_system_restore_point(description)
                elif tool == "restore_system_to_point":
                    point_id = params.get("point_id", "")
                    result = restore_system_to_point(point_id)
                elif tool == "get_system_performance_counters":
                    result = get_system_performance_counters()
                elif tool == "get_system_event_logs":
                    result = get_system_event_logs()
                elif tool == "clear_system_event_logs":
                    result = clear_system_event_logs()
                elif tool == "get_system_registry_info":
                    result = get_system_registry_info()
                elif tool == "backup_system_registry":
                    result = backup_system_registry()
                elif tool == "restore_system_registry":
                    backup_path = params.get("backup_path", "")
                    result = restore_system_registry(backup_path)
                elif tool == "get_system_service_status":
                    service_name = params.get("service_name", "")
                    result = get_system_service_status(service_name)
                elif tool == "get_system_startup_items":
                    result = get_system_startup_items()
                elif tool == "add_system_startup_item":
                    name = params.get("name", "")
                    path = params.get("path", "")
                    result = add_system_startup_item(name, path)
                elif tool == "remove_system_startup_item":
                    name = params.get("name", "")
                    result = remove_system_startup_item(name)
                elif tool == "get_system_environment_variables":
                    result = get_system_environment_variables()
                elif tool == "set_system_environment_variable":
                    name = params.get("name", "")
                    value = params.get("value", "")
                    result = set_system_environment_variable(name, value)
                elif tool == "delete_system_environment_variable":
                    name = params.get("name", "")
                    result = delete_system_environment_variable(name)
                elif tool == "get_system_timezone":
                    result = get_system_timezone()
                elif tool == "set_system_timezone":
                    timezone_name = params.get("timezone_name", "")
                    result = set_system_timezone(timezone_name)
                elif tool == "get_system_locale_settings":
                    result = get_system_locale_settings()
                elif tool == "set_system_locale":
                    locale_name = params.get("locale_name", "")
                    result = set_system_locale(locale_name)
                elif tool == "get_system_language_settings":
                    result = get_system_language_settings()
                elif tool == "set_system_language":
                    language_code = params.get("language_code", "")
                    result = set_system_language(language_code)
                elif tool == "get_system_keyboard_layout":
                    result = get_system_keyboard_layout()
                elif tool == "set_system_keyboard_layout":
                    layout_code = params.get("layout_code", "")
                    result = set_system_keyboard_layout(layout_code)
                elif tool == "get_system_mouse_settings":
                    result = get_system_mouse_settings()
                elif tool == "set_system_mouse_settings":
                    speed = params.get("speed", 10)
                    acceleration = params.get("acceleration", True)
                    result = set_system_mouse_settings(speed, acceleration)
                elif tool == "get_system_display_settings":
                    result = get_system_display_settings()
                elif tool == "set_system_display_settings":
                    brightness = params.get("brightness", 100)
                    contrast = params.get("contrast", 50)
                    result = set_system_display_settings(brightness, contrast)
                elif tool == "get_system_audio_settings":
                    result = get_system_audio_settings()
                elif tool == "set_system_audio_settings":
                    volume = params.get("volume", 50)
                    mute = params.get("mute", False)
                    result = set_system_audio_settings(volume, mute)
                elif tool == "get_system_power_settings":
                    result = get_system_power_settings()
                elif tool == "set_system_power_settings":
                    scheme = params.get("scheme", "balanced")
                    timeout = params.get("timeout", 60)
                    result = set_system_power_settings(scheme, timeout)
                elif tool == "get_system_security_settings":
                    result = get_system_security_settings()
                elif tool == "set_system_security_settings":
                    enhanced_security = params.get("enhanced_security", True)
                    result = set_system_security_settings(enhanced_security)
                elif tool == "get_system_privacy_settings":
                    result = get_system_privacy_settings()
                elif tool == "set_system_privacy_settings":
                    data_collection = params.get("data_collection", False)
                    location_tracking = params.get("location_tracking", False)
                    result = set_system_privacy_settings(data_collection, location_tracking)
                elif tool == "get_system_updates_settings":
                    result = get_system_updates_settings()
                elif tool == "set_system_updates_settings":
                    auto_updates = params.get("auto_updates", True)
                    download_only = params.get("download_only", False)
                    result = set_system_updates_settings(auto_updates, download_only)
                elif tool == "get_system_backup_settings":
                    result = get_system_backup_settings()
                elif tool == "set_system_backup_settings":
                    auto_backup = params.get("auto_backup", True)
                    backup_location = params.get("backup_location", "C:\\Backup")
                    result = set_system_backup_settings(auto_backup, backup_location)
                elif tool == "get_system_network_settings":
                    result = get_system_network_settings()
                elif tool == "set_system_network_settings":
                    proxy_server = params.get("proxy_server", "")
                    dns_server = params.get("dns_server", "")
                    result = set_system_network_settings(proxy_server, dns_server)
                elif tool == "get_system_wifi_settings":
                    result = get_system_wifi_settings()
                elif tool == "set_system_wifi_settings":
                    ssid = params.get("ssid", "")
                    password = params.get("password", "")
                    auto_connect = params.get("auto_connect", True)
                    result = set_system_wifi_settings(ssid, password, auto_connect)
                elif tool == "get_system_bluetooth_settings":
                    result = get_system_bluetooth_settings()
                elif tool == "set_system_bluetooth_settings":
                    enabled = params.get("enabled", True)
                    discoverable = params.get("discoverable", True)
                    result = set_system_bluetooth_settings(enabled, discoverable)
                elif tool == "get_system_usb_settings":
                    result = get_system_usb_settings()
                elif tool == "set_system_usb_settings":
                    auto_install_drivers = params.get("auto_install_drivers", True)
                    power_saving = params.get("power_saving", True)
                    result = set_system_usb_settings(auto_install_drivers, power_saving)
                elif tool == "get_system_printer_settings":
                    result = get_system_printer_settings()
                elif tool == "set_system_printer_settings":
                    default_printer = params.get("default_printer", "")
                    print_quality = params.get("print_quality", "normal")
                    result = set_system_printer_settings(default_printer, print_quality)
                elif tool == "get_system_camera_settings":
                    result = get_system_camera_settings()
                elif tool == "set_system_camera_settings":
                    resolution = params.get("resolution", "1080p")
                    frame_rate = params.get("frame_rate", 30)
                    result = set_system_camera_settings(resolution, frame_rate)
                elif tool == "get_system_microphone_settings":
                    result = get_system_microphone_settings()
                elif tool == "set_system_microphone_settings":
                    sensitivity = params.get("sensitivity", 50)
                    noise_reduction = params.get("noise_reduction", True)
                    result = set_system_microphone_settings(sensitivity, noise_reduction)
                elif tool == "get_system_speaker_settings":
                    result = get_system_speaker_settings()
                elif tool == "set_system_speaker_settings":
                    volume = params.get("volume", 75)
                    bass = params.get("bass", 50)
                    treble = params.get("treble", 50)
                    result = set_system_speaker_settings(volume, bass, treble)
                elif tool == "get_system_game_settings":
                    result = get_system_game_settings()
                elif tool == "set_system_game_settings":
                    high_performance = params.get("high_performance", True)
                    vsync = params.get("vsync", False)
                    result = set_system_game_settings(high_performance, vsync)
                elif tool == "get_system_developer_settings":
                    result = get_system_developer_settings()
                elif tool == "set_system_developer_settings":
                    developer_mode = params.get("developer_mode", True)
                    usb_debugging = params.get("usb_debugging", False)
                    result = set_system_developer_settings(developer_mode, usb_debugging)
                elif tool == "get_system_admin_settings":
                    result = get_system_admin_settings()
                elif tool == "set_system_admin_settings":
                    admin_password = params.get("admin_password", "")
                    result = set_system_admin_settings(admin_password)
                elif tool == "get_system_advanced_settings":
                    result = get_system_advanced_settings()
                elif tool == "set_system_advanced_settings":
                    advanced_features = params.get("advanced_features", True)
                    result = set_system_advanced_settings(advanced_features)
                elif tool == "get_system_hidden_settings":
                    result = get_system_hidden_settings()
                elif tool == "set_system_hidden_settings":
                    enable_hidden = params.get("enable_hidden", True)
                    result = set_system_hidden_settings(enable_hidden)
                elif tool == "get_system_registry_advanced":
                    result = get_system_registry_advanced()
                elif tool == "set_system_registry_advanced":
                    key_path = params.get("key_path", "")
                    value_name = params.get("value_name", "")
                    value_data = params.get("value_data", "")
                    result = set_system_registry_advanced(key_path, value_name, value_data)
                elif tool == "get_system_performance_advanced":
                    result = get_system_performance_advanced()
                elif tool == "set_system_performance_advanced":
                    ram_boost = params.get("ram_boost", True)
                    cpu_priority = params.get("cpu_priority", "normal")
                    result = set_system_performance_advanced(ram_boost, cpu_priority)
                elif tool == "get_system_network_advanced":
                    result = get_system_network_advanced()
                elif tool == "set_system_network_advanced":
                    buffer_size = params.get("buffer_size", 64)
                    connection_timeout = params.get("connection_timeout", 30)
                    result = set_system_network_advanced(buffer_size, connection_timeout)
                elif tool == "get_system_security_advanced":
                    result = get_system_security_advanced()
                elif tool == "set_system_security_advanced":
                    real_time_protection = params.get("real_time_protection", True)
                    firewall_level = params.get("firewall_level", "high")
                    result = set_system_security_advanced(real_time_protection, firewall_level)
                elif tool == "get_system_privacy_advanced":
                    result = get_system_privacy_advanced()
                elif tool == "set_system_privacy_advanced":
                    app_tracking = params.get("app_tracking", False)
                    diagnostic_data = params.get("diagnostic_data", "minimal")
                    result = set_system_privacy_advanced(app_tracking, diagnostic_data)
                elif tool == "get_system_updates_advanced":
                    result = get_system_updates_advanced()
                elif tool == "set_system_updates_advanced":
                    auto_download = params.get("auto_download", True)
                    schedule_time = params.get("schedule_time", "02:00")
                    result = set_system_updates_advanced(auto_download, schedule_time)
                elif tool == "get_system_backup_advanced":
                    result = get_system_backup_advanced()
                elif tool == "set_system_backup_advanced":
                    backup_frequency = params.get("backup_frequency", "daily")
                    retention_days = params.get("retention_days", 30)
                    result = set_system_backup_advanced(backup_frequency, retention_days)
                elif tool == "get_system_display_advanced":
                    result = get_system_display_advanced()
                elif tool == "set_system_display_advanced":
                    color_temperature = params.get("color_temperature", 6500)
                    refresh_rate = params.get("refresh_rate", 60)
                    result = set_system_display_advanced(color_temperature, refresh_rate)
                elif tool == "get_system_audio_advanced":
                    result = get_system_audio_advanced()
                elif tool == "set_system_audio_advanced":
                    sample_rate = params.get("sample_rate", 44100)
                    bit_depth = params.get("bit_depth", 16)
                    result = set_system_audio_advanced(sample_rate, bit_depth)
                elif tool == "get_system_power_advanced":
                    result = get_system_power_advanced()
                elif tool == "set_system_power_advanced":
                    cpu_governor = params.get("cpu_governor", "performance")
                    gpu_boost = params.get("gpu_boost", True)
                    result = set_system_power_advanced(cpu_governor, gpu_boost)
                elif tool == "get_system_gpu_advanced":
                    result = get_system_gpu_advanced()
                elif tool == "set_system_gpu_advanced":
                    overclock_gpu = params.get("overclock_gpu", False)
                    memory_clock = params.get("memory_clock", 1000)
                    result = set_system_gpu_advanced(overclock_gpu, memory_clock)
                elif tool == "get_system_cpu_advanced":
                    result = get_system_cpu_advanced()
                elif tool == "set_system_cpu_advanced":
                    overclock_cpu = params.get("overclock_cpu", False)
                    voltage = params.get("voltage", 1.2)
                    result = set_system_cpu_advanced(overclock_cpu, voltage)
                elif tool == "get_system_memory_advanced":
                    result = get_system_memory_advanced()
                elif tool == "set_system_memory_advanced":
                    timing = params.get("timing", "auto")
                    voltage = params.get("voltage", 1.35)
                    result = set_system_memory_advanced(timing, voltage)
                elif tool == "get_system_storage_advanced":
                    result = get_system_storage_advanced()
                elif tool == "set_system_storage_advanced":
                    trim_enabled = params.get("trim_enabled", True)
                    cache_size = params.get("cache_size", 1024)
                    result = set_system_storage_advanced(trim_enabled, cache_size)
                elif tool == "get_system_network_card_advanced":
                    result = get_system_network_card_advanced()
                elif tool == "set_system_network_card_advanced":
                    speed = params.get("speed", "auto")
                    duplex = params.get("duplex", "auto")
                    result = set_system_network_card_advanced(speed, duplex)
                elif tool == "get_system_wifi_card_advanced":
                    result = get_system_wifi_card_advanced()
                elif tool == "set_system_wifi_card_advanced":
                    channel = params.get("channel", 6)
                    power = params.get("power", 100)
                    result = set_system_wifi_card_advanced(channel, power)
                elif tool == "get_system_bluetooth_card_advanced":
                    result = get_system_bluetooth_card_advanced()
                elif tool == "set_system_bluetooth_card_advanced":
                    power_level = params.get("power_level", 7)
                    connection_timeout = params.get("connection_timeout", 30)
                    result = set_system_bluetooth_card_advanced(power_level, connection_timeout)
                elif tool == "get_system_usb_controller_advanced":
                    result = get_system_usb_controller_advanced()
                elif tool == "set_system_usb_controller_advanced":
                    power_management = params.get("power_management", True)
                    bandwidth_limit = params.get("bandwidth_limit", 100)
                    result = set_system_usb_controller_advanced(power_management, bandwidth_limit)
                elif tool == "get_system_audio_controller_advanced":
                    result = get_system_audio_controller_advanced()
                elif tool == "set_system_audio_controller_advanced":
                    sample_rate = params.get("sample_rate", 48000)
                    buffer_size = params.get("buffer_size", 1024)
                    result = set_system_audio_controller_advanced(sample_rate, buffer_size)
                elif tool == "get_system_video_controller_advanced":
                    result = get_system_video_controller_advanced()
                elif tool == "set_system_video_controller_advanced":
                    color_depth = params.get("color_depth", 32)
                    refresh_rate = params.get("refresh_rate", 75)
                    result = set_system_video_controller_advanced(color_depth, refresh_rate)
                elif tool == "get_system_printer_advanced":
                    result = get_system_printer_advanced()
                elif tool == "set_system_printer_advanced":
                    dpi = params.get("dpi", 600)
                    paper_size = params.get("paper_size", "A4")
                    result = set_system_printer_advanced(dpi, paper_size)
                elif tool == "get_system_camera_advanced":
                    result = get_system_camera_advanced()
                elif tool == "set_system_camera_advanced":
                    exposure = params.get("exposure", 50)
                    iso = params.get("iso", 100)
                    result = set_system_camera_advanced(exposure, iso)
                elif tool == "get_system_microphone_advanced":
                    result = get_system_microphone_advanced()
                elif tool == "set_system_microphone_advanced":
                    gain = params.get("gain", 50)
                    sample_rate = params.get("sample_rate", 44100)
                    result = set_system_microphone_advanced(gain, sample_rate)
                elif tool == "get_system_speaker_advanced":
                    result = get_system_speaker_advanced()
                elif tool == "set_system_speaker_advanced":
                    crossover_frequency = params.get("crossover_frequency", 1000)
                    bass_management = params.get("bass_management", True)
                    result = set_system_speaker_advanced(crossover_frequency, bass_management)
                elif tool == "get_system_game_advanced":
                    result = get_system_game_advanced()
                elif tool == "set_system_game_advanced":
                    frame_limit = params.get("frame_limit", 60)
                    texture_quality = params.get("texture_quality", "high")
                    result = set_system_game_advanced(frame_limit, texture_quality)
                elif tool == "get_system_developer_advanced":
                    result = get_system_developer_advanced()
                elif tool == "set_system_developer_advanced":
                    debug_mode = params.get("debug_mode", True)
                    performance_profiling = params.get("performance_profiling", True)
                    result = set_system_developer_advanced(debug_mode, performance_profiling)
                elif tool == "get_system_admin_advanced":
                    result = get_system_admin_advanced()
                elif tool == "set_system_admin_advanced":
                    enable_remote_access = params.get("enable_remote_access", True)
                    audit_log_level = params.get("audit_log_level", "medium")
                    result = set_system_admin_advanced(enable_remote_access, audit_log_level)
                elif tool == "get_system_advanced_all":
                    result = get_system_advanced_all()
                elif tool == "set_system_advanced_all":
                    result = set_system_advanced_all()
                elif tool == "get_system_hidden_advanced":
                    result = get_system_hidden_advanced()
                elif tool == "set_system_hidden_advanced":
                    result = set_system_hidden_advanced()
                elif tool == "get_system_registry_hidden":
                    result = get_system_registry_hidden()
                elif tool == "set_system_registry_hidden":
                    result = set_system_registry_hidden()
                elif tool == "get_system_performance_hidden":
                    result = get_system_performance_hidden()
                elif tool == "set_system_performance_hidden":
                    result = set_system_performance_hidden()
                elif tool == "get_system_network_hidden":
                    result = get_system_network_hidden()
                elif tool == "set_system_network_hidden":
                    result = set_system_network_hidden()
                elif tool == "get_system_security_hidden":
                    result = get_system_security_hidden()
                elif tool == "set_system_security_hidden":
                    result = set_system_security_hidden()
                elif tool == "get_system_privacy_hidden":
                    result = get_system_privacy_hidden()
                elif tool == "set_system_privacy_hidden":
                    result = set_system_privacy_hidden()
                elif tool == "get_system_updates_hidden":
                    result = get_system_updates_hidden()
                elif tool == "set_system_updates_hidden":
                    result = set_system_updates_hidden()
                elif tool == "get_system_backup_hidden":
                    result = get_system_backup_hidden()
                elif tool == "set_system_backup_hidden":
                    result = set_system_backup_hidden()
                elif tool == "get_system_display_hidden":
                    result = get_system_display_hidden()
                elif tool == "set_system_display_hidden":
                    result = set_system_display_hidden()
                elif tool == "get_system_audio_hidden":
                    result = get_system_audio_hidden()
                elif tool == "set_system_audio_hidden":
                    result = set_system_audio_hidden()
                elif tool == "get_system_power_hidden":
                    result = get_system_power_hidden()
                elif tool == "set_system_power_hidden":
                    result = set_system_power_hidden()
                elif tool == "get_system_gpu_hidden":
                    result = get_system_gpu_hidden()
                elif tool == "set_system_gpu_hidden":
                    result = set_system_gpu_hidden()
                elif tool == "get_system_cpu_hidden":
                    result = get_system_cpu_hidden()
                elif tool == "set_system_cpu_hidden":
                    result = set_system_cpu_hidden()
                elif tool == "get_system_memory_hidden":
                    result = get_system_memory_hidden()
                elif tool == "set_system_memory_hidden":
                    result = set_system_memory_hidden()
                elif tool == "get_system_storage_hidden":
                    result = get_system_storage_hidden()
                elif tool == "set_system_storage_hidden":
                    result = set_system_storage_hidden()
                elif tool == "get_system_network_card_hidden":
                    result = get_system_network_card_hidden()
                elif tool == "set_system_network_card_hidden":
                    result = set_system_network_card_hidden()
                elif tool == "get_system_wifi_card_hidden":
                    result = get_system_wifi_card_hidden()
                elif tool == "set_system_wifi_card_hidden":
                    result = set_system_wifi_card_hidden()
                elif tool == "get_system_bluetooth_card_hidden":
                    result = get_system_bluetooth_card_hidden()
                elif tool == "set_system_bluetooth_card_hidden":
                    result = set_system_bluetooth_card_hidden()
                elif tool == "get_system_usb_controller_hidden":
                    result = get_system_usb_controller_hidden()
                elif tool == "set_system_usb_controller_hidden":
                    result = set_system_usb_controller_hidden()
                elif tool == "get_system_audio_controller_hidden":
                    result = get_system_audio_controller_hidden()
                elif tool == "set_system_audio_controller_hidden":
                    result = set_system_audio_controller_hidden()
                elif tool == "get_system_video_controller_hidden":
                    result = get_system_video_controller_hidden()
                elif tool == "set_system_video_controller_hidden":
                    result = set_system_video_controller_hidden()
                elif tool == "get_system_printer_hidden":
                    result = get_system_printer_hidden()
                elif tool == "set_system_printer_hidden":
                    result = set_system_printer_hidden()
                elif tool == "get_system_camera_hidden":
                    result = get_system_camera_hidden()
                elif tool == "set_system_camera_hidden":
                    result = set_system_camera_hidden()
                elif tool == "get_system_microphone_hidden":
                    result = get_system_microphone_hidden()
                elif tool == "set_system_microphone_hidden":
                    result = set_system_microphone_hidden()
                elif tool == "get_system_speaker_hidden":
                    result = get_system_speaker_hidden()
                elif tool == "set_system_speaker_hidden":
                    result = set_system_speaker_hidden()
                elif tool == "get_system_game_hidden":
                    result = get_system_game_hidden()
                elif tool == "set_system_game_hidden":
                    result = set_system_game_hidden()
                elif tool == "get_system_developer_hidden":
                    result = get_system_developer_hidden()
                elif tool == "set_system_developer_hidden":
                    result = set_system_developer_hidden()
                elif tool == "get_system_admin_hidden":
                    result = get_system_admin_hidden()
                elif tool == "set_system_admin_hidden":
                    result = set_system_admin_hidden()
                elif tool == "get_system_all_hidden":
                    result = get_system_all_hidden()
                elif tool == "set_system_all_hidden":
                    result = set_system_all_hidden()
                elif tool == "chat":
                    result = params.get("text", "")
                    log(f"{Fore.GREEN}AI: {result}{Style.RESET_ALL}", Fore.GREEN)
                else:
                    result = f"[UNKNOWN TOOL] {tool}"
                
                results.append(result)
                time.sleep(0.1)  # Reduced delay for speed
            
            # Save AI response
            final_response = " | ".join(str(r) for r in results if r)
            history[-1]["ai"] = final_response
            if not any(a.get("tool") == "chat" for a in parse_advanced_response(advanced_response)):
                log(f"{Fore.GREEN}AI: {final_response}{Style.RESET_ALL}", Fore.GREEN)
            
            save_history(history)
            
        except KeyboardInterrupt:
            log("\n[!] Interrupted by user", Fore.RED)
            break
        except Exception as e:
            log(f"[CRITICAL ERROR] {str(e)}", Fore.RED)
    
    # Cleanup
    if driver:
        driver.quit()
    log("\n[✓] Ultimate Humanity Assistant stopped. Goodbye!", Fore.GREEN)

if __name__ == "__main__":
    main()
