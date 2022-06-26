import pytest
from .pages.product_page import ProductPage

def test_compare_price_and_title(browser): # Совпадает ли название и цена товара с тем что лежит в корзине
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.button_located()
    page.solve_quiz()
    page.compare_price()
    page.compare_title()

def test_success_message(browser): # Наличие сообщения об успешной покупке
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.button_located()
    page.solve_quiz()
    page.element_is_present()


# Поиск страницы, на которой присутствует баг.
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.button_located()
    page.solve_quiz()
    page.compare_price()
    page.compare_title()

    # Тесты помеченные xfail являются негативными кейсами, и они должны провалится.

@pytest.mark.xfail # Сообщение об успешной покупке не должно присутствовать, после добавления товара
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.button_located()
    page.solve_quiz()
    page.success_is_not_presented()

def test_guest_cant_see_success_message(browser): # Сообщение об успешной покупке не должно присутствовать
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.success_is_not_presented()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): # Сообщение о покупке исчезает
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.button_located()
    page.solve_quiz()
    page.element_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser): # Должна присутствовать кнопка логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()