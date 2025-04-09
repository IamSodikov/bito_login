from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10
        self.browser.implicitly_wait(self.timeout)

    def open(self, url):
        self.browser.get(url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def click_element(self, how, what):
        self.browser.find_element(how, what).click()

    def input_text(self, how, what, text):
        self.browser.find_element(how, what).send_keys(text)

    def get_current_url(self):
        return self.browser.current_url

    def wait_until_url_changes(self, old_url, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.url_changes(old_url))

    def clear_and_slow_input(self, how, what, text):
        element = self.browser.find_element(how, what)
        element.clear()
        time.sleep(0.5)
        for char in text:
            element.send_keys(char)
            time.sleep(0.2)
