import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")

@pytest.fixture
def browser(request):
    browser_language = request.config.getoption("language")
    browser = None
    if browser_language == "en":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)

    else:
        browser_language == "ru"
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        browser = webdriver.Chrome(options=options)


    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
