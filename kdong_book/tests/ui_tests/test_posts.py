from api.auth_api import AuthAPI
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import sys
print (sys.path)

def test_register_by_api_then_login_ui(api_context, page, new_user_data):
    #1 - Dùng API register tạo user mới
    auth_api = AuthAPI(api_context)
    user = auth_api.register_user(new_user_data)
    assert user is not None

    #2 - Dùng user vừa tạo login trên UI
    login = LoginPage(page)
    login.open()
    login.login(new_user_data["email"], new_user_data["password"])

    #VP - Verify login thành công khi có success message displays
    assert DashboardPage(page).is_login_success_message_visible(), "Lỗi: Thông báo đăng nhập thành công không hiển thị!"
