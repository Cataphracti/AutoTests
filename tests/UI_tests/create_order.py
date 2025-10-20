from selenium.webdriver.common.by import By
from pages.smsd_gv_order_creation_interface import Gv_Crt_Ordr
from pages.smsd_homepage import SMSD_HomePage


def test_order_creation(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gv_auth()
    order_page = Gv_Crt_Ordr(browser)
    order_page.p1()
    order_page.p2()
    order_page.cargo()
    order_page.weight()
    order_page.calculate()
    check_calculation = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/h3')
    assert check_calculation.text == 'Текущий расчёт'
    browser.quit()