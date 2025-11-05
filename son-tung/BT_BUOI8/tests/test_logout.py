import json

from BT_BUOI8.components.header_component import HeaderComponent
from BT_BUOI8.pages.login_page import LoginPage

def test_logout(page):
    login_page = LoginPage(page)
    header_component = HeaderComponent(page)

    # Login
    with open("BT_BUOI8/data/users.json") as f:
        user = json.load(f)

    valid = user["valid_user"]

    login_page.login(valid["username"], valid["password"])
    login_page.assert_login_successful()

    header_component.logout()