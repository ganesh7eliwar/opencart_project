import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.read_config import ReadConfigRP
# from pytest_metadata.plugin import metadata_key
from datetime import datetime

now = datetime.now().strftime("%d%m%Y%H%M%S")
URL = ReadConfigRP.url()

""" ############################################# BROWSER SETUP #################################################### """

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_argument('--start-maximized')
chrome_serv_manager = Service(ChromeDriverManager().install())

headless_option = webdriver.ChromeOptions()
headless_option.add_experimental_option('excludeSwitches', ['enable-logging'])
headless_option.add_argument('--headless')

firefox_serv_manager = Service(GeckoDriverManager().install())


# edge_serv_manager = Service(EdgeChromiumDriverManager().install())


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print('\nTest Run on Chrome Browser.')
        driver = webdriver.Chrome(service=chrome_serv_manager, options=chrome_options)
    elif browser == 'firefox':
        print('\nTest Run on Firefox Browser.')
        driver = webdriver.Firefox(service=firefox_serv_manager)
    # elif browser == 'edge':
    #     print('\nTest Run on Edge Browser.')
    #     driver = webdriver.Edge(service=edge_serv_manager)
    else:
        print('\nTest Run on Headless Browser.')
        driver = webdriver.Chrome(service=chrome_serv_manager, options=headless_option)
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.quit()


""" ######################################### HTML REPORT GENERATION ############################################### """


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.stash.setdefault(metadata_key, {})  # Initializes the stash entry if not already present
#     config.stash[metadata_key]['Project'] = 'OpenKart'
#     config.stash[metadata_key]['Module Name'] = 'User Registration'
#     config.stash[metadata_key]['Tester'] = 'Ganesh'
#     config.stash[metadata_key]['Environment'] = 'Staging'


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config._metadata = {
#         "Project": "OpenKart",
#         "Module Name": "User Registration",
#         "Tester": "Ganesh",
#         "Environment": "Staging"
#     }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('Platform', None)
    metadata.pop('JAVA_HOME', None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = f'./reports/html_report_{now}.html'
    config.option.self_contained_html = True
