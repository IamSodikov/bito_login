from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import chromedriver_autoinstaller
from dotenv import load_dotenv

load_dotenv()

def before_all(context):
    print("▶ Headless holat aniqlanmoqda...")
    
    # ChromeDriver'ni avtomatik yuklash
    chromedriver_autoinstaller.install()

    chrome_options = Options()

    if os.getenv("HEADLESS", "false").lower() == "true":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')
        print("▶ Headless rejimda ishga tushyapti...")
    else:
        chrome_options.add_argument('--start-maximized')
        print("▶ Real brauzer rejimda ishga tushyapti...")

    context.browser = webdriver.Chrome(options=chrome_options)

def after_all(context):
    if hasattr(context, "browser"):
        context.browser.quit()
