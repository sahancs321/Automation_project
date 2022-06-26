import time
from .base_page import  BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def button_located(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def compare_price(self):
        original_price = self.browser.find_element(*ProductPageLocators.ORIGINAL_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == original_price.text, "price doesn't match"

    def compare_title(self):
        basket_title = self.browser.find_element(*ProductPageLocators.BASKET_TITLE)
        original_title = self.browser.find_element(*ProductPageLocators.ORIGINAL_TITLE)
        assert basket_title.text == original_title.text, "title doesn't match"

    def success_is_not_presented(self):
        assert self.is_not_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Element exists, but shouldn't"

    def element_is_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Element doesn't exist"

    def element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Element is not disappeared"