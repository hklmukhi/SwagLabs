from locators.inventory_locators import InventoryLocators
from utilities.waits import Waits

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.waits = Waits(driver)

    def get_page_title(self):
        return self.waits.wait_for_visibility(InventoryLocators.PAGE_TITLE).text

    def add_backpack_to_cart(self):
        self.waits.wait_for_clickable(InventoryLocators.ADD_TO_CART_BACKPACK).click()

    def click_cart_icon(self):
        self.waits.wait_for_clickable(InventoryLocators.CART_ICON).click()
