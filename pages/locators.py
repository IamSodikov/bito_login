from selenium.webdriver.common.by import By

class LoginPageLocators:
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@name='phone_number']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
