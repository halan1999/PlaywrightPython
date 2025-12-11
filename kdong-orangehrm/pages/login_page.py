from playwright.sync_api import sync_playwright
from playwright.sync_api import Page,expect
import re
from core.base_page import BasePage
from pages.social_network_page import SocialNetworkPage
from config.social_network_links_enum import SocialNetworkLinks

class LoginPage(BasePage):
    LINKEDIN_ICON_LINK = ('xpath', "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']")
    FACEBOOK_ICON_LINK = ('xpath', "//a[@href='https://www.facebook.com/OrangeHRM/']")
    TWITTER_ICON_LINK = ('xpath', "//a[contains(@href, 'twitter.com/orangehrm')]") 
    YOUTUBE_ICON_LINK = ('xpath', "//a[contains(@href, 'youtube.com/c/OrangeHRMInc')]")
    PAGE_TITLE_EXPECTED = "OrangeHRM"

    # Business Actions
    def go_to_page(self, url:str):
        self._visit(url)
        expect(self.page).to_have_title(self.PAGE_TITLE_EXPECTED)
        print(f"Đã truy cập thành công: {url}")

    def open_social_link(self, social_link_type: SocialNetworkLinks) -> Page:
        """
        Mở liên kết mạng xã hội bằng cách sử dụng đối tượng Enum đã được đóng gói.
        
        :param social_link_type: Thành viên của Enum SocialNetworkLinks.
        :return: Đối tượng Page của tab mới.
        """
        
        # 1. Lấy Locator từ Enum
        locator_to_use = social_link_type.link_locator
        
        # 2. Lấy Tên hiển thị từ Enum (ví dụ: "TWITTER")
        link_name = social_link_type.name
        
        # 3. Thực thi hành động
        new_page = self._open_new_tab(
            locator=locator_to_use,
            name=link_name
        )
        
        # (Tùy chọn) Kiểm chứng URL cơ bản ngay trong Page Object (Kiểm tra nhanh)
        # Bằng cách sử dụng thông tin đóng gói trong Enum
        expect(new_page).to_have_url(
        re.compile(social_link_type.expected_url), # KHÔNG dùng regexp=
        timeout=5000, 
        # Các options khác (ví dụ: ignoreCase) nếu cần, nhưng timeout là đủ
    )
        
        return new_page
    def click_social_link_and_verify(self, locator_tuple: tuple[str, str], expected_url_part: str):
        """
        Thực hiện hành động: 2. click lên social links --> trả về social_page: expected new tab mở ra 
        
        Args:
            locator_tuple: Tuple chứa loại selector và giá trị.
            expected_url_part: Phần URL mong đợi của trang mới.
        """
        selector_type, selector_value = locator_tuple
        
        # Sử dụng Playwright's "wait_for_event('popup')" để bắt tab mới
        # và dùng 'with' để quản lý ngữ cảnh và tránh lỗi race condition.
        with self.page.expect_popup() as popup_info:
            # 2. Click lên social link
            if selector_type == 'xpath':
                self.page.locator(selector_value).click()
            elif selector_type == 'css':
                self.page.locator(selector_value).click()

        # Lấy đối tượng Page mới (tab mới)
        new_page = popup_info.value

        # Verify Point: Kiểm tra tab mới đã mở ra và URL chính xác
        print(f"    - Verify: New tab opened and URL contains '{expected_url_part}'")
        expected_regex = re.compile(re.escape(expected_url_part))
        expect(new_page).to_have_url(expected_regex)
        return new_page

    def close_new_tab(self, new_page: Page):
        """
        Thực hiện hành động: 4. đóng tab ở step 3
        
        Args:
            new_page: Đối tượng Page của tab cần đóng.
        """
        new_page.close()
        # Verify Point: Kiểm tra tab cũ vẫn còn hoạt động
        expect(self.page).to_have_title(self.PAGE_TITLE_EXPECTED)
        print("    - Action: New tab closed, returned to the old tab.")
    
    def get_social_links(self) -> list[tuple[str, str, str]]:
        """Trả về danh sách các link mạng xã hội (tên, locator, URL mong đợi)"""
        # Đây là cấu trúc dữ liệu để lặp qua trong test case
        return [
            ("LinkedIn", self.LINKEDIN_ICON_LINK, "linkedin.com"),
            ("Facebook", self.FACEBOOK_ICON_LINK, "facebook.com/OrangeHRM/"),
            ("Twitter", self.TWITTER_ICON_LINK, "x.com/orangehrm"),
            ("YouTube", self.YOUTUBE_ICON_LINK, "youtube.com/c/OrangeHRMInc"),
        ]
    
    