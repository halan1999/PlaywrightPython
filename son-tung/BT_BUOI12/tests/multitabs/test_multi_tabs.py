from BT_BUOI12.pages.multitabs.new_social_page import NewWindowPage
from BT_BUOI12.pages.multitabs.window_page import WindowPage

def test_multi_tabs(windows_page):

    # Tab chính đã được mở sẵn từ fixture
    main_page = windows_page
    main_page.open_url()

    # Kiểm tra nội dung trên tab chính
    heading_main = main_page.get_heading_text()
    assert heading_main == "Login"

    # Mở tab mới và nhận về POM NewWindowPage
    new_window_page: NewWindowPage = main_page.open_new_tab_and_return_page_object(WindowPage.click_linkedin)

    # Thao tác trên tab mới
    heading_linkedin = new_window_page.get_heading_text("OrangeHRM")
    assert heading_linkedin == "OrangeHRM"

    main_page._bring_to_front()
    # assert main_page.get_heading_text() == ""

    new_window_page: NewWindowPage = main_page.open_new_tab_and_return_page_object(WindowPage.click_facebook)
    heading_facebook = new_window_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_facebook

    main_page._bring_to_front()
    new_window_page: NewWindowPage = main_page.open_new_tab_and_return_page_object(WindowPage.click_twitter)
    heading_twitter = new_window_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_twitter

    main_page._bring_to_front()
    new_window_page: NewWindowPage = main_page.open_new_tab_and_return_page_object(WindowPage.click_youtube)
    heading_youtube = new_window_page.get_heading_text("OrangeHRM")
    assert "OrangeHRM" in heading_youtube