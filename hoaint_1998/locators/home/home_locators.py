from core.common_locators import CommonLocators as CL

class HomeLocators:
    WELCOM_LABLE = "//h6[starts-with(text(), 'Welcom') and contains(text(), 'hello')]"
    LOGOUT_BUTTON = f"//div[@class='page-header']{CL._normalize_space_xpath("a", "Logout")}"