from selenium.webdriver.common.by import By
from datetime import datetime

timestamp = datetime.now().strftime("%d%m%Y%H%M%S")


class LoginPage:
    email_add_id = 'input-email'
    password_id = 'input-password'
    login_btn_xpath = "//input[@value='Login']"
    cnf_text_id = 'content'
    alert_msg_css_selector = '.alert-dismissible'
    logout_btn_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def e_mail_address(self, email):
        email_add = self.driver.find_element(By.ID, self.email_add_id)
        email_add.send_keys(email)

    def password_textbox(self, pass_wd):
        email_password = self.driver.find_element(By.ID, self.password_id)
        email_password.send_keys(pass_wd)

    def login_button(self):
        login_btn = self.driver.find_element(By.XPATH, self.login_btn_xpath)
        login_btn.click()

    def confirmation_txt(self):
        cnf_text = self.driver.find_element(By.ID, self.cnf_text_id)
        cnf_text.screenshot(f'./screenshots/test_login_page_03_pass_{timestamp}.png')

    def alert_message(self):
        alert_msg = self.driver.find_element(By.CSS_SELECTOR, self.alert_msg_css_selector)
        alert_msg.screenshot(f'./screenshots/test_login_page_03_fail_{timestamp}.png')

    def logout_button(self):
        logout_btn = self.driver.find_element(By.LINK_TEXT, self.logout_btn_link_text)
        logout_btn.click()