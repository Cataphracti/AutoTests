from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    order_page.continue_order_creation()
    # order_page.insert_max_weight() -- Шаг внесения максимальной суточной разгрузки. На доработке
    order_page.accept_contract()
    order_page.cargo_price_per_ton()
    order_page.shipping_conditions()
    order_page.publish()
    wait = WebDriverWait(browser, 4)
    wait.until(EC.url_contains('https://smartseeds.ru/carriage/orders?tab=orders&status-tab=in-progress'))
    browser.quit()