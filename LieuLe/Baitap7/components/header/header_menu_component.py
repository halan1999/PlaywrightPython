from core.base_page import BasePage
from components.left_menu.base_menu_component import BaseMenuComponent

class HeaderMenuComponent(BasePage):

    MENU_PARENT = "xpath=//li[contains(@class,'dropdown') and contains(@class,'pc-h-item')]"
    TOGGLE = "xpath=.//a[contains(@class,'dropdown-toggle')]"
    SUB_MENU = "xpath=.//div[contains(@class,'dropdown-menu')]//a"

    def get_all_menus(self):
        menus = []
        parents = self.page.locator(self.MENU_PARENT)

        print("HEADER MENU COUNT =", parents.count())

        for i in range(parents.count()):
            el = parents.nth(i)
            name = el.inner_text().strip() or f"header_menu_{i}"

            menus.append(
                BaseMenuComponent(
                    self.page,
                    el.locator(self.TOGGLE),
                    name,
                    self.SUB_MENU
                )
            )
        return menus

    def capture_all(self, folder="screenshots/header_menu"):
        for menu in self.get_all_menus():
            try:
                menu.capture(folder)
            except Exception as e:
                print(f"⚠ Không thể chụp header menu {menu.name}: {e}")
