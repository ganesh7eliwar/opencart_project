import pytest
from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage
from pageobjects.register_page import RegisterPage
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigLP


class TestLogin:
    expected_title = ReadConfigLP.expected_title()
    email = ReadConfigLP.email()
    password = ReadConfigLP.password()
    log = LoggenClass.log_generator()

    @pytest.mark.sanity
    def test_login_page_03(self, setup):

        self.driver = setup
        self.log.info('********** Test Session Started. **********')
        self.hp = HomePage(self.driver)
        self.hp.my_account_dd()
        self.log.info('Clicked on my_account dropdown button.')
        self.hp.login_btn()
        self.log.info('Clicked on login button.')

        self.lp = LoginPage(self.driver)
        self.lp.e_mail_address(self.email)
        self.log.info(f'Inserted data into Email textbox. --> {self.email}')
        self.lp.password_textbox(self.password)
        self.log.info(f'Inserted data into first name textbox. --> {self.password}')
        self.lp.login_button()
        self.log.info('Clicked on login button.')

        self.rp = RegisterPage(self.driver)

        if self.driver.title == self.expected_title:
            self.log.info('Entered into if Block')
            self.lp.confirmation_txt()
            self.log.info('Captured Screenshot')
            self.rp.my_account_dd()
            self.log.info('Clicked on my account button')
            self.rp.logout_btn()
            self.log.info('Clicked on log out button')
            self.log.info('Testcase Passed')
            assert True

        else:
            self.log.info('Entered into else Block')
            self.lp.alert_message()
            self.log.info('Captured screenshot')
            self.log.info('Testcase Failed')
            assert False

        self.log.info('========== Test Session Finished. ==========')
