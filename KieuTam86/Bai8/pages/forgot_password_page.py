from core.base_page import BasePage


class ForgotPassword(BasePage):

    title_locator = "//h4[normalize-space() = 'Reset your password']"
    title = "Reset your password"
    title_display = 'Reset your password'
    email_locator = "//input[@placeholder='Email address']"
    btn_reset_password = ".ladda-label"
    click_here = ".f-w-400"


    def __init__(self, page):
        super().__init__(page)

    def check_form_forgot_password(self):
        self._verify_locator_visible(self.title_locator)
        self._verify_text(self.title_locator, self.title)
        self._verify_locator_visible(self.email_locator)
        self._verify_locator_visible(self.btn_reset_password)