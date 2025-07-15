from datetime import datetime

from selenium.webdriver.common.by import By

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")


class CheckURL:
    page_header_link_text = 'Qafox.com'

    def __init__(self, driver):
        self.driver = driver

    def page_header(self):
        header = self.driver.find_element(By.LINK_TEXT, self.page_header_link_text)
        header.screenshot(f'./screenshots/test_url_pass{timestamp}.png')

    def fail_ss(self):
        screenshot = self.driver.save_screenshot(f'./screenshots/test_url_fail{timestamp}.png')
        return screenshot
