import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def get_options():
    print('\n --- get_options ---')
    options: Options = Options()
    options.add_argument('chrome')  # use  'headless' run without UI
    options.add_argument('--window-size=1200,800')
    return options

@pytest.fixture
def get_webdriver(get_options) -> webdriver:
    print('\n --- get_webdriver ---')
    options: Options = get_options
    driver = webdriver.Chrome(executable_path='src/chromedriver.exe', options=options)
    return driver


# scope='function'- start for each test.
# scope='session'- start once for all sessions
@pytest.fixture(scope='function')
def setup(request, get_webdriver: webdriver):
    print('\n --- setup ---')
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('\n --- yield setup ---')
    driver.close()
    driver.quit()
