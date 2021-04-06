import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: en or ru')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.getoption('language')
    browser = None
    if browser_name == 'chrome' and user_language == 'ru' or user_language == 'en':
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome of firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()