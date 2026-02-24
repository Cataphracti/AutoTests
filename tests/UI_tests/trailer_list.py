from selenium.webdriver.common.by import By
from pages.smsd_homepage import SMSD_HomePage
from pages.gp_interface import Gp_Interface

def test_open_trailers_list(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gp_auth()
    gp_page = Gp_Interface(browser)
    #gp_page.close_reminder_popup()
    gp_page.click_trailers_button()
    check_trailers_list = browser.find_element(By.CSS_SELECTOR, '#app > div > div.interior > div.interior__content > div.interior__body > div > div > div.d-flex.justify-content-between > div > div.ui-textbox__content > label > input')
    assert check_trailers_list.get_attribute('placeholder') == 'Номер прицепа'
    browser.quit()