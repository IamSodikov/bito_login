from .base_page import BasePage
from .locators import LoginPageLocators
from config import LOGIN_URL
import time

class LoginPage(BasePage):
    def open_login_page(self):
        self.open(LOGIN_URL)

    def enter_credentials(self, phone, password):
        self.clear_and_slow_input(*LoginPageLocators.PHONE_NUMBER_INPUT, phone)
        time.sleep(1)
        self.input_text(*LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
