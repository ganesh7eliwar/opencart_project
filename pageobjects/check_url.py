from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from datetime import datetime
import allure

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")


class CheckURL:
    page_header_link_text = 'Qafox.com'

    def __init__(self, driver):
        self.driver = driver

    def page_header(self):
        header = self.driver.find_element(By.LINK_TEXT, self.page_header_link_text)
        header.screenshot(f'./screenshots/test_url_pass_{timestamp}.png')

    def fail_ss(self):
        screenshot = self.driver.save_screenshot(f'./screenshots/test_url_fail_{timestamp}.png')
        return screenshot

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Url_Pass_{timestamp}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Url_Fail_{timestamp}',
                      attachment_type=AttachmentType.PNG)
