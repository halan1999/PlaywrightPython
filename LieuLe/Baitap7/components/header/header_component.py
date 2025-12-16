# components/header/header_component.py
import os
from core.base_page import BasePage


class HeaderComponent(BasePage):

    MENU_ITEMS = "//ul[contains(@class,'navbar-nav')]/li"

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.root_folder = "screenshots/header"

    def get_menus(self):
        menus = self.page.locator(self.MENU_ITEMS)
        count = menus.count()
        print("FOUND MENUS:", count)
        menu_list = []

        for i in range(count):
            element = menus.nth(i)
            name = element.inner_text().strip().replace("\n", "_")

            has_submenu = element.locator(".//ul").count()

            if has_submenu > 0:
                menu_list.append(DropdownMenuComponent(self.page, element, name))
            else:
                menu_list.append(SimpleMenuComponent(self.page, element, name))

        return menu_list

    def capture_all(self):
        menus = self.get_menus()

        for menu in menus:
            folder = os.path.join(self.root_folder, menu.name)
            os.makedirs(folder, exist_ok=True)

            if isinstance(menu, SimpleMenuComponent):
                menu.capture(folder)
            else:
                menu.expand()
                menu.capture(folder)
                menu.capture_submenus(folder)
