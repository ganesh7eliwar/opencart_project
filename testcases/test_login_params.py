from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigLP
import allure
from pytest import mark


class TestLoginParams:
    expected_title = ReadConfigLP.expected_title()
    log = LoggenClass.log_generator()

    @allure.epic('Opencart Project')
    @allure.feature('Parameterized Test')
    @allure.story('Verify Login with Data')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('smoke', 'login')
    @allure.link('https://tutorialsninja.com/demo/', 'Login')
    @allure.title('Your Test')
    @allure.description('This is a Parameterized test which gives different Inputs while Login.')
    @mark.sanity
    @mark.regression
    def test_login_params(self, setup, data_for_login):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info('Driver Setup Successful.')
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.status_list = []

        self.hp.my_account_dd()
        self.log.info('Clicked on my_account dropdown button.')
        self.hp.login_btn()
        self.log.info('Clicked on login button.')
        self.lp.user_email(data_for_login[0])
        self.log.info(f'Inserted data into Email textbox. --> {data_for_login[0]}')
        self.lp.user_password(data_for_login[1])
        self.log.info(f'Inserted data into first name textbox. --> {data_for_login[1]}')
        self.lp.login_button()
        self.log.info('Clicked on login button.')

        if data_for_login[2] == 'Pass':
            self.log.info('Entered into if Block')
            if self.driver.title == self.expected_title:
                self.log.info('Entered into Nested if Block')
                self.status_list.append('Pass')
                self.log.info('Appended data to Status List.')
                self.lp.logout_button()
                self.log.info('Clicked on log out button')
            else:
                self.log.info('Entered into Else Block.')
                self.status_list.append('Fail')
                self.log.info('Appended data to Status List.')

        elif data_for_login[2] == 'Fail':
            self.log.info('Entered into Elif Block.')
            if self.driver.title == self.expected_title:
                self.log.info('Entered into If Block within Elif Block.')
                self.status_list.append('Fail')
                self.log.info('Appended data to Status List.')
                self.lp.logout_button()
                self.log.info('Clicked on Logout Button if Logged In.')
            else:
                self.log.info('Entered into Else Block.')
                self.status_list.append('Pass')
                self.log.info('Appended Data to Status List.')

        if 'Fail' not in self.status_list:
            self.log.info('Entered into If Block for Assertion.')
            self.log.info('If Fail not in Status List Testcase Passed.')
            self.log.info(f'Status List: {self.status_list}')
            assert True
        else:
            self.log.info('Entered into Else Block For Assertion.')
            self.log.info('If Fail in Status list Testcase Failed')
            self.log.info(f'Status List: {self.status_list}')
            assert False

        self.log.info('========== Test Session Finished. ==========')
