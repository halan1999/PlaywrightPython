from locators.common_locators import CommonLocators

class LoginPageLocators(CommonLocators):
    USERNAME_INPUT_LOCATOR = CommonLocators._input_by_attribute_xpath("id", "iusername")
    PASSWORD_INPUT_LOCATOR = CommonLocators._input_by_attribute_xpath("id", "ipassword")
    LOGIN_BUTTON_LOCATOR = CommonLocators._button_by_attribute_xpath("type", "submit")
    FORGOT_PASSWORD_LINK_LOCATOR = CommonLocators._contains_text_xpath("span", "Forgot password?")

    TOAST_ERROR_INVALID_CREDENTIALS = CommonLocators._contains_text_xpath("div", "Invalid Login Credentials")
    