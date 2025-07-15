from pageobjects.check_url import CheckURL
from utilities.logger import LoggenClass
from utilities.read_config import Url


class TestURL:
    log = LoggenClass.log_generator()

    def test_url(self, setup):
        self.log.info('********** Test Session Started. **********')
        self.driver = setup
        self.log.info(f'Title of the Page is: {self.driver.title}')
        self.cu = CheckURL(self.driver)

        if self.driver.title == Url.expected_url():
            self.log.info('Entered into if Block.')
            self.log.info('Testcase test_url Passed.')
            self.cu.page_header()
            self.log.info('Captured Screenshot')
            assert True
        else:
            self.log.info('Entered into else Block.')
            self.log.info('Testcase test_url Failed.')
            self.cu.fail_ss()
            self.log.info('Captured Screenshot')
            assert False

        self.log.info('========== Test Session Finished. ==========')
