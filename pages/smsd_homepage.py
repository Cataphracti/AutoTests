from selenium.webdriver.common.by import By
from pages import gv_credentials
from pages import gp_credentials

class SMSD_HomePage: ##Сущность домашней страницы сайта с описанными функциями и готовыми действиями для тестов

    def __init__(self, browser): ##Функция браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def open(self):
        self.browser.get('https://smartseeds.ru/') ##Открыть домашнюю стр.сайта

    def click_authorize_button(self):
        authorize_button = self.browser.find_element(By.CSS_SELECTOR, '#layout > header > div > div.header_TopInfo__531fs > div.header_menu___KQop > div.UserData_Wrapper__kg_ZO > div > button') #Поиск элемента на странице
        authorize_button.click()

    def gv_auth(self):
        fld_usrname = self.browser.find_element(By.CSS_SELECTOR, '#username')
        fld_pswrd = self.browser.find_element(By.CSS_SELECTOR, '#password')
        fld_auth = self.browser.find_element(By.CSS_SELECTOR, 'body > div.LoginForm_Modal__LAV9A > div > div > button.LoginForm_Button___0gbi')
        fld_usrname.send_keys(gv_credentials.usr)
        fld_pswrd.send_keys(gv_credentials.pswd)
        fld_auth.click()

    def gp_auth(self):
        fld_usrname = self.browser.find_element(By.CSS_SELECTOR, '#username')
        fld_pswrd = self.browser.find_element(By.CSS_SELECTOR, '#password')
        fld_auth = self.browser.find_element(By.CSS_SELECTOR, 'body > div.LoginForm_Modal__LAV9A > div > div > button.LoginForm_Button___0gbi')
        fld_usrname.send_keys(gp_credentials.usr)
        fld_pswrd.send_keys(gp_credentials.pswd)
        fld_auth.click()