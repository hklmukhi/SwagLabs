import pytest
from selenium import webdriver
from utilities.screenshots import ScreenshotUtil
import allure
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

    def pytest_sessionstart(session):
        print("\n ======Test Execution Started======")
        if not os.path.exists("allure-results"):
            os.makedirs("allure-results")
        with open("allure-results/environment.properties", "w") as f:
            f.write("Environment:QA\n")
            f.write("Browser = Chrome\n")
            f.write("URL: https://www.saucedemo.com\n")
            f.write("Framework: Pytest + Selenium")
            f.write("Tester: Hare Krishna")


    def pytest_sessionfinish(session, exitstatus):
        print("\n ======Test Execution finished======")

    def pytest_runtest_setup(item):
        print(f"\n Setup Starting Item :  {item.name}")

    @pytest.hookimpl(hookwrapper = True)
    def pytest_runtest_makereport(item,call):
        outcome = yield
        report = outcome.get_result()

        if report.when == 'call and report.failed':
            if 'driver' in item.funcargs:
                driver = item.funcargs["driver"]
                path = ScreenshotUtil.capture(driver,item.name)
                print(f"\n Screenshot Captures : {path}")
                allure.attach.file(path,name=f"{item.name}_failure_screenshot", attachment_type=allure.attachment_type.png)
                print(f"\nscreenshot captured and attached to allure:{path}")
