from core.common_locators import CommonLocators
from utils.messages import ERROR_MESSAGE

class LoginLocators:
    USERNAME_INPUT = CommonLocators._input_by_attribute_xpath("id", "iusername")
    PASSWORD_INPUT = CommonLocators._input_by_attribute_xpath("id", "ipassword")
    LOGIN_BUTTON = CommonLocators._button_by_attribute_xpath("type", "submit")
    FORGOT_PASSWORD_LINK = CommonLocators._contains_text_xpath("span", "Forgot password?")
    #---------Message-----------
    TOAST_MESSAGE_INVALID_CREDENTIALS = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['INVALID_CREDENTIALS']}")
    TOAST_MESSAGE_ERROR_PASSWORD_TOO_SHORT = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['ERROR_PASSWORD_TOO_SHORT']}")
    TOAST_MESSAGE_REQUIRED = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['REQUIRED_USERNAME_PASSWORD']}")