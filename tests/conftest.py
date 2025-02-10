from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture() ## Предусловие запуска браузера в автотестах: какой браузер, в каком режиме (оконный или полный и тд)
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3) ##  ожидания в случае долгой загрузки страницы
    yield browser