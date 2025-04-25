import pytest

from selenium.webdriver.common.by import By
import time
from pages.smsd_homepage import SMSDHomePage

def test_test(browser):
    home = SMSDHomePage(browser)
    home.open()
    time.sleep(1)
    home.click_authorize_button()
    time.sleep(1)
    title = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]')
    assert title.text == 'Вход'
