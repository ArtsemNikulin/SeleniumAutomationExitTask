from .base_page import BasePage
from .locators import BasePageLocators
from .locators import PageObjectLocators


class BasketPage(BasePage):
    def open_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket.click()

    def empty_basket(self):
        assert self.is_element_present(*PageObjectLocators.EMPTY_BASKET), 'is not empty'
