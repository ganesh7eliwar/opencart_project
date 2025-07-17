from selenium.webdriver.common.by import By
from datetime import datetime
from allure_commons.types import AttachmentType
import allure

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")


class RegisterPage:
    my_ac_dd_xpath = "//a[@title='My Account']"
    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_tb_id = "input-email"
    tel_id = "input-telephone"
    password_tb_id = "input-password"
    cnf_pass_tb_id = "input-confirm"
    newsletter_xpath = "//label[@class='radio-inline']/input[@value='1']"
    privacy_pol_cb_name = "agree"
    continue_btn_css_selector = ".btn-primary"
    confirmation_msg_xpath = "//div[@id='content']"
    warning_msg_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    logout_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def my_account_dd(self):
        my_acc_dd = self.driver.find_element(By.XPATH, self.my_ac_dd_xpath)
        my_acc_dd.click()

    def first_name(self, firstname):
        first_name_textbox = self.driver.find_element(By.ID, self.first_name_id)
        first_name_textbox.send_keys(firstname)

    def last_name(self, lastname):
        last_name_textbox = self.driver.find_element(By.ID, self.last_name_id)
        last_name_textbox.send_keys(lastname)

    def email_address(self, email):
        email_add_textbox = self.driver.find_element(By.ID, self.email_tb_id)
        email_add_textbox.send_keys(email)

    def telephone(self, telephone_no):
        telephone_textbox = self.driver.find_element(By.ID, self.tel_id)
        telephone_textbox.send_keys(telephone_no)

    def password_textbox(self, password):
        password_tb = self.driver.find_element(By.ID, self.password_tb_id)
        password_tb.send_keys(password)

    def confirm_password(self, cnf_pass):
        confirm_pass_tb = self.driver.find_element(By.ID, self.cnf_pass_tb_id)
        confirm_pass_tb.send_keys(cnf_pass)

    def news_letter_radio_btn(self):
        nl_radio_btn = self.driver.find_element(By.XPATH, self.newsletter_xpath)
        nl_radio_btn.click()

    def privacy_policy(self):
        privacy_pol_cb = self.driver.find_element(By.NAME, self.privacy_pol_cb_name)
        privacy_pol_cb.click()

    def continue_btn(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, self.continue_btn_css_selector)
        continue_button.click()

    def acc_creation_message(self):
        message = self.driver.find_element(By.XPATH, self.confirmation_msg_xpath)
        message.screenshot(f'./screenshots/test_register_page_02_pass_{timestamp}.png')

    def warning_message(self):
        warning = self.driver.find_element(By.XPATH, self.warning_msg_xpath)
        warning.screenshot(f'./screenshots/test_register_page_02_fail_{timestamp}.png')

    def logout_btn(self):
        logout_button = self.driver.find_element(By.LINK_TEXT, self.logout_link_text)
        logout_button.click()

    def allure_pass(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Registration_Pass_{timestamp}',
                      attachment_type=AttachmentType.PNG)

    def allure_fail(self):
        allure.attach(self.driver.get_screenshot_as_png(), name=f'Test_Registration_Fail_{timestamp}',
                      attachment_type=AttachmentType.PNG)