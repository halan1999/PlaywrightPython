from BT_BUOI8.pages.menu.manage_clients import ManageClients

def test_manage_clients(login_page):
    # Login
    login_page.login_user("valid_user")
    login_page.assert_login_successful()

    # Click open menu Manage Clients
    menu_manage_clients = ManageClients(login_page.page)
    menu_manage_clients.open_menu_button()
    menu_manage_clients.assert_open_successful()

    # Click button Add new
    menu_manage_clients.add_new_client()