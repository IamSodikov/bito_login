from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()

def before_all(context):
    chrome_options = Options()

    if os.getenv("HEADLESS", "false").lower() == "true":
        print("▶ Headless rejimda ishga tushyapti...")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
    else:
        print("▶ Vizual brauzer rejimida ishga tushyapti...")
        chrome_options.add_argument("--start-maximized")

    context.browser = webdriver.Chrome(options=chrome_options)

def after_all(context):
    context.browser.quit()
