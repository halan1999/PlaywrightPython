import os
import re
from core.base_page import BasePage

class BaseMenuComponent(BasePage):
    def __init__(self, page, element, name, submenu_selector=".//ul[contains(@class,'pc-submenu')]//li"):
        super().__init__(page)
        self.element = element
        self.name = name
        self.submenu_selector = submenu_selector

    def safe_name(self, max_len=20):
        """Loại bỏ ký tự không hợp lệ và rút gọn tên menu"""
        name = re.sub(r'[\\/*?:"<>|]', "", self.name)
        return name[:max_len].replace(" ", "_")

    def expand(self):
        """Mở menu cha nếu có submenu, tránh collapse"""
        try:
            if self.element.is_visible():
                # click mở submenu nếu chưa hiển thị
                submenus = self.element.locator(self.submenu_selector)
                if submenus.count() > 0 and not submenus.first.is_visible():
                    self.element.click()
                    self.page.wait_for_timeout(300)
        except Exception:
            pass

    def capture(self, folder):
        """Đệ quy chụp submenu nhiều cấp"""
        try:
            self.expand()
            submenu_locator = self.element.locator(self.submenu_selector)
            count = submenu_locator.count()

            for i in range(count):
                submenu = submenu_locator.nth(i)
                try:
                    submenu_name = submenu.inner_text().strip().replace("\n", "_")
                    submenu_folder = os.path.join(folder, re.sub(r'[\\/*?:"<>|]', "", submenu_name))
                    os.makedirs(submenu_folder, exist_ok=True)

                    if submenu.is_visible():
                        submenu.scroll_into_view_if_needed()
                        submenu.screenshot(path=os.path.join(submenu_folder, "index.png"))
                    else:
                        print(f"⚠ Submenu {submenu_name} không hiển thị, bỏ qua screenshot")

                    # tạo BaseMenuComponent cho submenu để đệ quy
                    sub_component = BaseMenuComponent(self.page, submenu, submenu_name, self.submenu_selector)
                    sub_component.capture(submenu_folder)

                except Exception as e:
                    print(f"⚠ Không thể chụp submenu {submenu_name}: {e}")

        except Exception as e:
            print(f"⚠ Lỗi capture submenu {self.name}: {e}")
    
    def get_submenus(self):
        """Trả về danh sách các submenu dưới menu này"""
        submenus = []
        try:
            items = self.element.locator(self.submenu_selector)
            count = items.count()
            for i in range(count):
                el = items.nth(i)
                name = el.inner_text().strip().replace("\n", "_")
                submenus.append(
                    BaseMenuComponent(
                        self.page,
                        el,
                        name,
                        submenu_selector=self.submenu_selector
                    )
                )
        except Exception as e:
            print(f"⚠ Lỗi khi lấy submenu của {self.name}: {e}")
        return submenus