from time import time

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.cart
def test_add_product_to_cart(driver):
    Login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    Login_page.login("standard_user","secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.click_cart_icon()
    #time.sleep(2)
    assert cart_page.get_cart_title() == "Your Cart"
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"