from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # автоматически скачает и добавит в PATH

@pytest.fixture() ## Предусловие запуска браузера в автотестах: какой браузер, в каком режиме (оконный или полный и тд)
def browser():
    options = Options()
    #options.add_argument('--headless')
    #options.page_load_strategy = 'none'
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(40) ## Ожидание в случае долгой загрузки страницы
    yield browser