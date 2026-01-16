# API Register --> API Login: Lấy accessToken --> UI Login với accessToken đó--> Kiểm tra login thành công
import allure
from pages.login_page import LoginPage
from playwright.sync_api import expect

@allure.epic("API → UI")
@allure.feature("Auth")
@allure.story("Login with accessToken (no UI login)")
def test_login_with_api_user(page, api_user):
    # Inject token trước khi load page
    page.add_init_script(
    f"window.localStorage.setItem('accessToken', '{api_user['token']}');"
)


    page.goto("/")

    # Verify user đã login
    expect(page.get_by_text("Dashboard")).to_be_visible()

