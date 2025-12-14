from core.common_locators import CommonLocators
from core.base_page import BasePage

class CalendarComponents(BasePage):
    # region Locator
    MONTH_LABEL = "//div[@class='dtp-date']/div[1]/div[contains(@class, 'dtp-actual-month')]"
    LEFT_MONTH_ICON = ""
    RIGHT_MONTH_ICON = ""
    YEAR_LABEL = ""
    LEFT_YEAR_ICON = ""
    RIGH_YEAR_ICON = ""
    
    # endregion

    def __init__(self, page):
        super().__init__(page)

    