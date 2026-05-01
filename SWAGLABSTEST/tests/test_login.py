import pytest
from pages.login_page import LoginPage
import allure


@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User Should get logged in")
@allure.description("Entering valid username and password to check user login")
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver):
    Login_page = LoginPage(driver)
    Login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

@allure.feature("Login")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User Should get logged in")
@allure.description("Entering invalid username and password to check user login")
@pytest.mark.regression
@pytest.mark.login
def test_invalid_login(driver):
    Login_page = LoginPage(driver)
    Login_page.login("wrong", "secret_sauce")

    assert "Epic sadface" in Login_page.get_error_message()
