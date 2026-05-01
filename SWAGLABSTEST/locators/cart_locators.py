from selenium.webdriver.common.by import By

class CartLocators:
    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    