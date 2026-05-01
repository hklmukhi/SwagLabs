from locators.login_locators import LoginLocators
from utilities.waits import Waits

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.waits = Waits(driver)

    def enter_username(self,username):
        self.waits.wait_for_visibility(LoginLocators.USERNAME).send_keys(username)

    def enter_password(self,password):
        self.waits.wait_for_visibility(LoginLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.waits.wait_for_clickable(LoginLocators.LOGIN_BUTTON).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.waits.wait_for_visibility(LoginLocators.ERROR_MESSAGE).text