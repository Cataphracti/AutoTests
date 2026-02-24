from selenium.webdriver.common.by import By
from pages.smsd_homepage import SMSD_HomePage
from pages.gp_interface import Gp_Interface
from pages.gp_eq_interface import EQ_interface

def test_open_specific_terminal(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gp_auth()
    gp_page = Gp_Interface(browser)
    eq_page = EQ_interface(browser)
    #gp_page.close_reminder_popup()
    gp_page.click_eq_button()
    eq_page.eq_choose_NZT()
    check_terminal_choice = browser.find_element(By.CSS_SELECTOR, '#app > div > div.interior.interior--frame > div.interior__content > div.interior__body > div > div > div.scTerminal-content > div.scPlan > div > div.vxe-table--render-wrapper > div.vxe-table--layout-wrapper > div.vxe-table--viewport-wrapper > div.vxe-table--main-wrapper.sx--true.sy--true > div.vxe-table--header-wrapper.body--wrapper > div > table > thead > tr > th.vxe-table--column.vxe-header--column.col_3.fixed--visible.fixed--width.is--padding.p-0 > div > div > span > span > div > span')
    assert check_terminal_choice.text == 'Пшеница'
    browser.quit()
