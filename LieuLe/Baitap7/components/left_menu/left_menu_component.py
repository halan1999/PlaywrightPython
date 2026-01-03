import os
import re
from core.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class LeftMenuComponent(BasePage):

    MENU_PARENT = "xpath=//ul[contains(@class,'pc-navbar')]//li[contains(@class,'pc-item')]"
    PARENT_TOGGLE = "xpath=//a[contains(@class,'sidenav-toggle')]"
    SUB_MENU_ITEM = "xpath=//ul[contains(@class,'pc-submenu')]//li[contains(@class,'pc-item')]"
    SUB_MENU_LINK = "xpath=//a[contains(@class,'pc-link') and not(contains(@class,'sidenav-toggle'))]"

    def _safe_name(self, text: str, max_len=30):
        text = re.sub(r'[\\/*?:"<>|]', "", text)
        return text.strip().replace(" ", "_")[:max_len]

    # ------------------------
    # 1. Capture ROOT MENU (FULL PAGE)
    # ------------------------
    def capture_parent_menus(self, folder):
        os.makedirs(folder, exist_ok=True)
        parents = self.page.locator(self.MENU_PARENT)

        for i in range(parents.count()):
            item = parents.nth(i)
            name = self._safe_name(item.inner_text())

            try:
                # Click root menu (load page if any)
                item.locator("xpath=.//a[1]").click(timeout=2000)
                self.page.wait_for_timeout(500)

                path = os.path.join(folder, f"{name}.png")
                self.page.screenshot(path=path, full_page=True)
                print(f"✅ Đã chụp menu cha: {path}")

            except PlaywrightTimeoutError:
                print(f"⚠ Can not capture root menu: {name} (skip)")
            except Exception as e:
                print(f"⚠ Error root menu  {name}: {e}")

    # ------------------------
    # 2. CAPTURE SUBMENU (FULL PAGE)
    # ------------------------
    def capture_submenus(self, folder):
        parents = self.page.locator(self.MENU_PARENT)

        for i in range(parents.count()):
            parent = parents.nth(i)
            parent_name = self._safe_name(parent.inner_text())

            submenu_items = parent.locator(self.SUB_MENU_ITEM)
            if submenu_items.count() == 0:
                continue  # menu not child → skip

            # Open root menu to click submenu
            try:
                parent.locator(self.PARENT_TOGGLE).click(timeout=2000)
                self.page.wait_for_timeout(300)
            except Exception:
                print(f"⚠ Can not open submenu of {parent_name}, skip")
                continue

            sub_folder = os.path.join(folder, parent_name)
            os.makedirs(sub_folder, exist_ok=True)

            for j in range(submenu_items.count()):
                submenu = submenu_items.nth(j)

                try:
                    link = submenu.locator(self.SUB_MENU_LINK)
                    sub_name = self._safe_name(submenu.inner_text())

                    link.click(timeout=2000)
                    self.page.wait_for_timeout(500)

                    path = os.path.join(sub_folder, f"{sub_name}.png")
                    self.page.screenshot(path=path, full_page=True)
                    print(f"✅ Capture submenu: {path}")

                except PlaywrightTimeoutError:
                    print(f"⚠ Can not capture submenu {parent_name} → {submenu.inner_text().strip()} (skip)")
                except Exception as e:
                    print(f"⚠ Error submenu {parent_name}: {e}")
