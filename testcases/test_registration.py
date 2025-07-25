from pytest import mark
from pageobjects.register_page import RegisterPage
from pageobjects.home_page import HomePage
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigRP
from utilities.generator import Generator
import allure


class TestLoginPage:
    expected_title = ReadConfigRP.expected_title()
    first_name = Generator.first_name()
    last_name = Generator.last_name()
    email = Generator.generate_email()
    telephone = Generator.telephone()
    password = Generator.password()
    log = LoggenClass.log_generator()

    @allure.epic('Opencart Project')
    @allure.feature('Registration')
    @allure.story('Registering a user for the first time.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('sanity', 'regression')
    @allure.link('https://tutorialsninja.com/demo/', 'Login')
    @allure.title('Your Test')
    @allure.description('This is a registration test.')
    @mark.sanity
    @mark.regression
    def test_register(self, setup):

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
            self.rp.allure_pass()
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
            self.rp.allure_fail()
            self.log.info('Testcase Failed')
            assert False

        self.log.info('========== Test Session Finished. ==========')
