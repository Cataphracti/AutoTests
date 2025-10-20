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
    gp_page.close_reminder_popup()
    gp_page.click_eq_button()
    eq_page.eq_choose_NZT()
    check_terminal_choice = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/table/thead/tr/th[2]/div/span/div/span')
    assert check_terminal_choice.text == 'Пшеница'

