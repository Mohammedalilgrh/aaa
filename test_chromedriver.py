# test_chromedriver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\deepseek\New folder\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print("✅ ChromeDriver is working!")
driver.quit()