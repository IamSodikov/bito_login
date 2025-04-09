from behave import given, when, then
from pages.login_page import LoginPage
from config import VALID_PHONE, VALID_PASSWORD

@given('Foydalanuvchi login sahifasida')
def step_open_login(context):
    context.page = LoginPage(context.browser)
    context.page.open_login_page()

@when('U to‘g‘ri email va parolni kiritadi')
def step_enter_credentials(context):
    context.page.enter_credentials(VALID_PHONE, VALID_PASSWORD)

@when('U "Kirish" tugmasini bosadi')
def step_click_login(context):
    context.page.click_login()

@then('U bosh sahifaga muvaffaqiyatli yo‘naltiriladi')
def step_check_redirect(context):
    old_url = context.page.get_current_url()
    context.page.wait_until_url_changes(old_url)
    new_url = context.page.get_current_url()
    assert "dashboard" in new_url, f"Dashboard sahifasiga o'tilmadi, hozirgi URL: {new_url}"
    