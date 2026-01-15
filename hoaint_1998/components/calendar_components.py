from core.common_locators import CommonLocators
from core.base_page import BasePage

class CalendarComponents(BasePage):
    # region Locator
    CALENDAR_ACTIVE = "//div[@class='dtp animated fadeIn']"
    MONTH_LABEL = f"{CALENDAR_ACTIVE}//div[contains(@class, 'dtp-actual-month')]"
    LEFT_MONTH_ICON = f"{CALENDAR_ACTIVE}//a[contains(@class, 'dtp-select-month-before')]"
    RIGHT_MONTH_ICON = f"{CALENDAR_ACTIVE}//a[contains(@class, 'dtp-select-month-after')]"
    YEAR_LABEL = f"{CALENDAR_ACTIVE}//div[contains(@class, 'dtp-actual-year')]"
    LEFT_YEAR_ICON = f"{CALENDAR_ACTIVE}//a[contains(@class, 'dtp-select-year-before')]"
    RIGH_YEAR_ICON = f"{CALENDAR_ACTIVE}//a[contains(@class, 'dtp-select-year-after')]"
    DAY_ICON = f"{CALENDAR_ACTIVE}//tbody//a[normalize-space()='30']"
    OK_BUTTON = f"{CALENDAR_ACTIVE}//button[contains(@class, 'dtp-btn-ok')]"
    CANCEL_BUTTON = f"{CALENDAR_ACTIVE}//button[contains(@class, 'dtp-btn-cancel')]"
    CLEAR_BUTTON = f"{CALENDAR_ACTIVE}//button[contains(@class, 'dtp-btn-clear')]"
    NOW_BUTTON = f"{CALENDAR_ACTIVE}//button[contains(@class, 'dtp-btn-now')]"
    
    # endregion

    def __init__(self, page):
        super().__init__(page)

    def _choose_date(self, year: int, month: int, day: int):
        ui_year = int(self._inner_text(self.YEAR_LABEL))
        ui_month = self._inner_text(self.MONTH_LABEL)
        if year < ui_year:
            self._click(self.LEFT_YEAR_ICON)
        elif year > ui_year:
            self._click(self.RIGH_YEAR_ICON)