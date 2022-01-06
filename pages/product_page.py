from .base_page import BasePage
from .locators import PageObjectLocators


class PageObject(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*PageObjectLocators.ADD_TO_BASKET)
        basket.click()

    def what_added_tobasket(self):
        added_book_name = self.browser.find_element(*PageObjectLocators.ADDED_BOOK_NAME).text
        book_name = self.browser.find_element(*PageObjectLocators.BOOK_NAME).text
        print(added_book_name, book_name)
        assert added_book_name == book_name, "Different book's names"

    def price_check(self):
        book_price = self.browser.find_element(*PageObjectLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*PageObjectLocators.BASKET_PRICE).text
        assert book_price == basket_price, "Different prices"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PageObjectLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_disapper_success_message(self):
        assert self.is_disappeared(*PageObjectLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

