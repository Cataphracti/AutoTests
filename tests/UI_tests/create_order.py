from selenium.webdriver.common.by import By
from pages.smsd_gv_order_creation_interface import Gv_Crt_Ordr
from pages.smsd_homepage import SMSD_HomePage


def test_order_creation(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.username_auth()
    order_page = Gv_Crt_Ordr(browser)
    order_page.p1()
    order_page.p2()
    order_page.cargo()
    order_page.weight()
    order_page.calculate()
    check_calculation = browser.find_element(By.CSS_SELECTOR, '#ui-tab-a0a445a6 > div > div > div.calculation__body > div > div.calculation-empty.col-xs-12.col-sm-12.col-md-12.col-lg-7 > div > div.calculation-result.d-flex.flex-column.p-6.br-4.bg-white.fs-12.lh-17 > div.text-center > button > div.ui-ripple-ink')
    assert check_calculation.text == 'Продолжить'