import string
import time
import random

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_EMAIL), 'no email form'
        assert self.is_element_present(*LoginPageLocators.LOG_IN_PASSWORD), 'no password form'
        assert self.is_element_present(*LoginPageLocators.LOG_IN_BUTTON), 'no log in button'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), 'no register email form'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), 'no register password form'
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM), 'no register password confirm form'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), 'no register button'

    def register_new_user(self, password='Qgtypo90pl'):
        email = str(time.time()) + random.choice(string.ascii_letters) + "@fakemail.coms"
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
