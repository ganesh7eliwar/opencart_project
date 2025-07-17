import allure
import pytest
from pageobjects.check_url import CheckURL
from utilities.logger import LoggenClass
from utilities.read_config import Url


class TestURL:
    log = LoggenClass.log_generator()

    @allure.epic('Opencart Project')
    @allure.feature('Url')
    @allure.story('Verify Url')
    @allure.label('owner', 'ganesh_sateliwar')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'regression')
    @allure.link('https://tutorialsninja.com/demo/', 'Login')
    @allure.title('Your Test')
    @allure.description('This is to check whether the Url is working Properly or not.')
    @pytest.mark.sanity
    def test_url(self, setup):
        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info(f'Title of the Page is: {self.driver.title}')
        self.cu = CheckURL(self.driver)

        if self.driver.title == Url.expected_url():
            self.log.info('Entered into if Block.')
            self.log.info('Testcase test_url Passed.')
            self.cu.page_header()
            self.cu.allure_pass()
            self.log.info('Captured Screenshot')
            assert True
        else:
            self.log.info('Entered into else Block.')
            self.log.info('Testcase test_url Failed.')
            self.cu.fail_ss()
            self.cu.allure_fail()
            self.log.info('Captured Screenshot')
            assert False

        self.log.info('========== Test Session Finished. ==========')
