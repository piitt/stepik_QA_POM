from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    # link1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_tile_present()
    page.should_be_product_price_present()


@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket2(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_add_to_basket()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_tile_present()
    page.should_be_product_price_present()
