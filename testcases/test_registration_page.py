import pytest
from pageobjects.register_page import RegisterPage
from pageobjects.home_page import HomePage
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigRP
from utilities.email_generator import EmailGenerator


class TestLoginPage:
    expected_title = ReadConfigRP.expected_title()
    first_name = ReadConfigRP.first_name()
    last_name = ReadConfigRP.last_name()
    email = EmailGenerator.generate_email()
    telephone = ReadConfigRP.telephone()
    password = ReadConfigRP.password()
    log = LoggenClass.log_generator()

    @pytest.mark.sanity
    def test_register_page_02(self, setup):

        self.driver = setup
        self.log.info('********** Test Session Started. **********')
        self.hp = HomePage(self.driver)
        self.hp.my_account_dd()
        self.log.info('Clicked on my_account dropdown button.')
        self.hp.register_btn()
        self.log.info('Clicked on register button.')

        self.rp = RegisterPage(self.driver)
        self.rp.first_name(self.first_name)
        self.log.info(f'Inserted data into first name textbox. --> {self.first_name}')
        self.rp.last_name(self.last_name)
        self.log.info(f'Inserted data into last name textbox. --> {self.last_name}')
        self.rp.email_address(self.email)
        self.log.info(f'Inserted data into email textbox. --> {self.email}')
        self.rp.telephone(self.telephone)
        self.log.info(f'Inserted telephone number into telephone textbox. --> {self.telephone}')
        self.rp.password_textbox(self.password)
        self.log.info(f'Inserted password. --> {self.password}')
        self.rp.confirm_password(self.password)
        self.log.info(f'Inserted confirm password. --> {self.password}')
        self.rp.news_letter_radio_btn()
        self.log.info('Clicked on news letter radio button.')
        self.rp.privacy_policy()
        self.log.info('Clicked on privacy policy checkbox.')
        self.rp.continue_btn()
        self.log.info('Clicked on Continue Button.')

        if self.driver.title == self.expected_title:
            self.log.info('Entered into if Block')
            self.rp.acc_creation_message()
            self.log.info('Captured Screenshot')
            self.rp.my_account_dd()
            self.log.info('Clicked on my account button')
            self.rp.logout_btn()
            self.log.info('Clicked on log out button')
            self.log.info('Testcase Passed')
            assert True
        else:
            self.log.info('Entered into else Block')
            self.rp.warning_message()
            self.log.info('Captured screenshot')
            self.log.info('Testcase Failed')
            assert False

        self.log.info('========== Test Session Finished. ==========')
