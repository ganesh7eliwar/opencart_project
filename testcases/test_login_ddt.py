from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage
from pageobjects.register_page import RegisterPage
from utilities import excelutils
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigLP
from pytest import mark
import allure


class TestLoginDDT:
    file = './testdata/data_for_ddt.xlsx'
    log = LoggenClass.log_generator()

    @allure.epic('Opencart Project')
    @allure.feature('Data Driven Test')
    @allure.story('Verify Login with Data')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('smoke', 'login')
    @allure.link('https://tutorialsninja.com/demo/', 'Login')
    @allure.title('Your Test')
    @allure.description('This is a Data Driven test which gives different Inputs while Login.')
    @mark.sanity
    @mark.regression
    def test_login_ddt(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.rows = excelutils.total_rows(self.file, 'Sheet1')
        self.log.info(f'Number of Rows in Table: {self.rows} including Header.')
        self.status_list = []
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.iteration = 0

        for r in range(2, self.rows + 1):

            self.iteration += 1
            self.log.info(f'Entered into for loop, Interation No.: {self.iteration}.')
            self.email = excelutils.read_data(self.file, 'Sheet1', r, 1)
            self.password = excelutils.read_data(self.file, 'Sheet1', r, 2)
            self.expected_result = excelutils.read_data(self.file, 'Sheet1', r, 3)

            self.hp.my_account_dd()
            self.log.info('Clicked on My Account Button.')
            self.hp.login_btn()
            self.log.info('Clicked on Login Button.')
            self.lp.user_email(self.email)
            self.log.info(f'Entered Email Address: {self.email}.')
            self.lp.user_password(self.password)
            self.log.info(f'Entered Password: {self.password}.')
            self.lp.login_button()
            self.log.info(f'Clicked on Login Button.')

            if self.expected_result == 'Pass':
                self.log.info('Entered into If Block.')
                if self.driver.title == ReadConfigLP.expected_title():
                    self.log.info('Entered into Nested If Block within If Block.')
                    self.status_list.append('Pass')
                    self.log.info('Appended data to Status List.')
                    self.lp.logout_button()
                    self.log.info('Clicked on Logout Button.')
                else:
                    self.log.info('Entered into Else Block.')
                    self.status_list.append('Fail')
                    self.log.info('Appended data to Status List.')

            elif self.expected_result == 'Fail':
                self.log.info('Entered into Elif Block.')
                if self.driver.title == ReadConfigLP.expected_title():
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
