from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find ("login")!=-1, "Current url is not login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.should_be_login_page()
        self.input_value(*LoginPageLocators.EMAIL_FIELD, email)
        self.input_value(*LoginPageLocators.PASSWORD_FIELD, password)
        self.input_value(*LoginPageLocators.REPEAT_PASSWORD_FIELD, password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit_button.click()


