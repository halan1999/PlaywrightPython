
from Core.config import HRM_USERNAME,HRM_PASSWORD

def test_login_success(login_page):
    login_page.open()
    login_page.login(HRM_USERNAME, HRM_PASSWORD)
    login_page.assert_login_success()