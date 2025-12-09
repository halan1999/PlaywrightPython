from BT_BUOI12.pages.multitabs.new_social_page import NewPage
from BT_BUOI12.pages.multitabs.orangehrm_page import OrangePage

def test_multi_tabs(windows_page):

    main_page = windows_page
    main_page.open_url()

    # Assert on main tab
    heading_main = main_page.get_heading_text()
    assert heading_main == "Login"

    # Open new tab and return POM NewPage
    new_page: NewPage = main_page.open_new_tab_and_return_page_object(OrangePage.click_linkedin)

    # Do on new tab
    heading_linkedin = new_page.get_heading_text("OrangeHRM")
    assert heading_linkedin == "OrangeHRM"
    main_page._bring_to_front()
    # assert main_page.get_heading_text() == ""

    new_page: NewPage = main_page.open_new_tab_and_return_page_object(OrangePage.click_facebook)
    heading_facebook = new_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_facebook

    main_page._bring_to_front()
    new_page: NewPage = main_page.open_new_tab_and_return_page_object(OrangePage.click_twitter)
    heading_twitter = new_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_twitter
    new_page.verify_element()

    main_page._bring_to_front()
    new_page: NewPage = main_page.open_new_tab_and_return_page_object(OrangePage.click_youtube)
    heading_youtube = new_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_youtube

    main_page._bring_to_front()
    main_page.login()
    main_page.verify_element()
    main_page.logout()