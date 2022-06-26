from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ORIGINAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ORIGINAL_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TITLE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

