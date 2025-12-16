from core.base_page import BasePage
from components.left_menu.base_menu_component import BaseMenuComponent

class LeftMenuComponent(BasePage):

    MENU_PARENT = "xpath=//ul[contains(@class,'pc-navbar')]//li[contains(@class,'pc-item')]"

    def get_all_menus(self):
        menus = []
        parents = self.page.locator(self.MENU_PARENT)

        count = parents.count()
        for i in range(count):
            el = parents.nth(i)
            name = el.inner_text().strip().replace("\n", "_")
            menus.append(BaseMenuComponent(self.page, el, name))

        return menus

    def capture_all(self, folder="screenshots/left_menu"):
        for menu in self.get_all_menus():
            try:
                menu.capture(folder)
            except Exception as e:
                print(f"⚠ Không thể chụp menu {menu.name}: {e}")
