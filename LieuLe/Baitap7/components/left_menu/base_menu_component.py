from core.base_page import BasePage

class BaseMenuComponent(BasePage):

    SUB_MENU = "xpath=.//ul[contains(@class,'pc-submenu')]//li"

    def __init__(self, page, element, name, level=0):
        super().__init__(page)
        self.element = element
        self.name = name
        self.level = level

    def has_children(self):
        return self.element.locator(self.SUB_MENU).count() > 0

    def expand(self):
        self.element.click()
        self.wait(0.3)

    def capture_self(self, base_folder):
        path = f"{base_folder}/{self.name}/index.png"
        self.screenshot(path)

    def capture(self, base_folder):
        self.capture_self(base_folder)

        if not self.has_children():
            return

        self.expand()

        children = self.element.locator(self.SUB_MENU)

        count = children.count()
        for i in range(count):

            self.expand()
            children = self.element.locator(self.SUB_MENU)

            child = children.nth(i)
            child_name = child.inner_text().strip().replace("\n", "_").replace("/", "_")

            child_menu = BaseMenuComponent(
                self.page,
                child,
                child_name,
                self.level + 1
            )
            child.click()
            self.wait(1)
            child_menu.capture(f"{base_folder}/{self.name}")
