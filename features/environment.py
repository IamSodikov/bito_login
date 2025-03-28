from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def before_all(context):
    print("Brauzer ochilmoqda...")
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    context.browser = webdriver.Chrome(options=chrome_options)

def after_all(context):
    time.sleep(10)
    context.browser.quit()
    print("Brauzer yopildi.")
