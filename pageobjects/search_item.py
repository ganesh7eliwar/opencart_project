from selenium.webdriver.common.by import By
from datetime import datetime
from allure_commons.types import AttachmentType
import allure

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")

class SearchItem:
    search_txt_bx_name = "search"
    search_btn_xpath = "//button[@class='btn btn-default btn-lg']"
    total_items_xpath = "//div[@class='caption']/h4/a"
    items_id = "content"

    def __init__(self, driver):
        self.driver = driver

    def search_text_box(self, item_name):
        search_txt_box = self.driver.find_element(By.NAME, self.search_txt_bx_name)
        search_txt_box.click()
        search_txt_box.send_keys(item_name)

    def search_button(self):
        search_btn = self.driver.find_element(By.XPATH, self.search_btn_xpath)
        search_btn.click()

    def total_items(self):
        total_its = self.driver.find_elements(By.XPATH, self.total_items_xpath)
        item_list = [item.text for item in total_its]
        return item_list

    def results(self):
        result = self.driver.find_element(By.ID, self.items_id)
        result.screenshot(f'./screenshots/Search_Item_Pass_{timestamp}.png')

    def no_results(self):
        self.driver.save_screenshot(f'./screenshots/Search_Item_Fail_{timestamp}.png')

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Pass_Pass_{timestamp}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Search_Fail_{timestamp}',
                      attachment_type=AttachmentType.PNG)