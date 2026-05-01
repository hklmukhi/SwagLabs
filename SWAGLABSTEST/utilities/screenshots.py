import os
from datetime import datetime

class ScreenshotUtil:
    @staticmethod
    def capture(driver,test_name):
        if not os.path.exists("screenshots"):
            os.makedirs("Screenshots")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"Screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(path)
        return path