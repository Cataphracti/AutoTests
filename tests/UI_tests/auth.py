from selenium.webdriver.common.by import By
from pages.smsd_homepage import SMSD_HomePage


# def test_authmodal_open(browser):
#     home = SMSD_HomePage(browser)
#     home.open()
#     home.click_authorize_button()
#     title = browser.find_element(By.CSS_SELECTOR, 'body > div.LoginForm_Modal__LAV9A > div > div > div.LoginForm_Title__H7tk_')
#     assert title.text == 'Вход'


def test_gv_auth(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gv_auth()
    check_user = browser.find_element(By.CSS_SELECTOR, '#app > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__top > div > div.side__credentials > div.side__organization')
    assert check_user.text == 'ООО "АЛЬЯНС-ИКС"'
    browser.quit()

def test_gp_auth(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gp_auth()
    check_user = browser.find_element(By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__top > div > div.side__credentials > div.side__organization')
    assert check_user.text == 'АО "РОСТВЕРТОЛ"'
    browser.quit()
