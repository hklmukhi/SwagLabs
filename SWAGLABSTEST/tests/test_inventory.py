import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.inventory

def test_inventory_title(driver):
    Loing_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    Loing_page.login("standard_user","secret_sauce")
    assert inventory_page.get_page_title()=="Products"