from pytest import mark
from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage
from pageobjects.register_page import RegisterPage
from pageobjects.search_item import SearchItem
from utilities.logger import LoggenClass
from utilities.read_config import ReadConfigLP
from utilities.read_config import Search
import allure


class TestSearchItem:
    log = LoggenClass.log_generator()
    email = ReadConfigLP.email()
    password = ReadConfigLP.password()
    item = Search.item_name()
    expected_item = Search.expected_item()

    @allure.epic('Opencart Project')
    @allure.feature('Search Item')
    @allure.story('Search the Expected Item.')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('smoke')
    @allure.link('https://tutorialsninja.com/demo/index.php?route=product/search', 'Login')
    @allure.title('Search')
    @allure.description('This Feature enables users to Search for their Expected Item.')
    @mark.sanity
    @mark.smoke
    def test_search_item(self, setup):

        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.hp = HomePage(self.driver)
        self.hp.my_account_dd()
        self.log.info('Clicked on my_account dropdown button.')
        self.hp.login_btn()
        self.log.info('Clicked on login button.')

        self.lp = LoginPage(self.driver)
        self.lp.e_mail_address(self.email)
        self.log.info(f'Inserted data into Email textbox. --> {self.email}')
        self.lp.password_textbox(self.password)
        self.log.info(f'Inserted data into first name textbox. --> {self.password}.')
        self.lp.login_button()
        self.log.info('Clicked on login button.')

        self.si = SearchItem(self.driver)
        self.si.search_text_box(self.item)
        self.log.info(f'Inserted text into Search Text Box. --> {self.item}.')
        self.si.search_button()
        self.log.info('Clicked on Search Button.')

        if self.expected_item in self.si.total_items():
            self.log.info('Entered into if Block.')
            self.log.info(f'Item List: --> {self.si.total_items()}.')
            self.log.info(f'Expected Item: "{self.expected_item}" is in the Item List.')
            self.si.results()
            self.log.info('Captured Screenshot.')
            self.si.allure_pass()
            self.rp = RegisterPage(self.driver)
            self.rp.my_account_dd()
            self.log.info('Clicked on my account button.')
            self.rp.logout_btn()
            self.log.info('Clicked on log out button.')
            self.log.info('Testcase Passed.')
            assert True
        else:
            self.log.info('Entered into else Block.')
            self.si.no_results()
            self.log.info('Captured Screenshot.')
            self.si.allure_fail()
            self.log.info('Testcase Failed.')
            assert False

        self.log.info('========== Test Session Finished. ==========')
