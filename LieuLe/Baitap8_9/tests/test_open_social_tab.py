from utils.path_helper import get_avatar_path
# def test_open_footer_social_tab(login_page):  
#     login_page.open()             
#     tabs = login_page.open_social_tabs()
#     login_page.verify_social_tabs(tabs)

def test_verify_twitter (login_page):
    # Open login    
    login_page.open()
    # Open twitter tab
    twitter_tab = login_page.open_twitter_tab()
    login_page.verify_twitter_page(twitter_tab)
    # Back to login tab
    login_page.footer_component.back_to_login_tab()
    # Login
    dashboard_page = login_page.login_valid_user()
    # Verify dashboard
    dashboard_page.verify_dashboard_displayed()
    # Change avatar
    dashboard_page.user_menu.change_avatar("avatar.png")
    # Logout
    dashboard_page.user_menu.logout()
