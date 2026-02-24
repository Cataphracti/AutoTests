from selenium.webdriver.common.by import By
from pages.smsd_homepage import SMSD_HomePage
from pages.gp_interface import Gp_Interface

def test_open_vehicles_list(browser):
    home = SMSD_HomePage(browser)
    home.open()
    home.click_authorize_button()
    home.gp_auth()
    gp_page = Gp_Interface(browser)
    #gp_page.close_reminder_popup()
    gp_page.click_vehicles_button()
    check_vehicles_list = browser.find_element(By.CSS_SELECTOR, '#app > div > div.interior > div.interior__content > div.interior__body > div > div > div.d-flex.flex-wrap.justify-content-between > div.ui-textbox.ui-textbox--icon-position-left.ui-textbox--default.is-bordered.mb-4 > div.ui-textbox__content > label > input')
    assert check_vehicles_list.get_attribute('placeholder') == 'Номер т/с' # get_attribute('placeholder') эта строка нужна т.к. текст элемента который мы проверяем является плейсхолдером
    browser.quit()