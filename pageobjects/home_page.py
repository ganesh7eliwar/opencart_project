from selenium.webdriver.common.by import By


class HomePage:
    my_ac_dd_xpath = "//a[@title='My Account']"
    reg_btn_xpath = "//a[normalize-space()='Register']"
    login_btn_link_txt = "Login"

    def __init__(self, driver):
        self.driver = driver

    def my_account_dd(self):
        my_acc_dd = self.driver.find_element(By.XPATH, self.my_ac_dd_xpath)
        my_acc_dd.click()

    def register_btn(self):
        reg_button = self.driver.find_element(By.XPATH, self.reg_btn_xpath)
        reg_button.click()

    def login_btn(self):
        login_button = self.driver.find_element(By.LINK_TEXT, self.login_btn_link_txt)
        login_button.click()
