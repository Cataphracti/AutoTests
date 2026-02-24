from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import gv_credentials
from pages import gp_credentials

class SMSD_HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get('https://smartseeds.ru/')

    def click_authorize_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#layout > header > div > div.header_TopInfo__531fs > div.header_menu___KQop > div.UserData_Wrapper__kg_ZO > div > button')
        )).click()

    def gv_auth(self):
        fld_usrname = self.browser.find_element(By.CSS_SELECTOR, '#username')
        fld_pswrd = self.browser.find_element(By.CSS_SELECTOR, '#password')
        fld_usrname.send_keys(gv_credentials.usr)
        fld_pswrd.send_keys(gv_credentials.pswd)
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.LoginForm_Modal__LAV9A > div > div > button.LoginForm_Button___0gbi')
        )).click()

    def gp_auth(self):
        fld_usrname = self.browser.find_element(By.CSS_SELECTOR, '#username')
        fld_pswrd = self.browser.find_element(By.CSS_SELECTOR, '#password')
        fld_usrname.send_keys(gp_credentials.usr)
        fld_pswrd.send_keys(gp_credentials.pswd)
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.LoginForm_Modal__LAV9A > div > div > button.LoginForm_Button___0gbi')
        )).click()