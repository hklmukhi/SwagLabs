from locators.cart_locators import CartLocators
from utilities.waits import Waits

class CartPage:
    def __init__(self,driver):
        self.driver = driver
        self.waits = Waits(driver)

    def get_cart_title(self):
        return self.waits.wait_for_visibility(CartLocators.CART_TITLE).text
    
    
    def get_cart_item_name(self):
        return self.waits.wait_for_visibility(CartLocators.CART_ITEM).text