from selenium.webdriver.common.by import By

class Gv_Crt_Ordr:

    def __init__(self, browser): ##Функция браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser


    def p1(self):
        p1 = self.browser.find_element(By.CSS_SELECTOR, '#ui-tab-3504f93b > div > div > div.calculation__bar.mb-4 > div > form > div:nth-child(1) > div:nth-child(1) > div')
        p1.click()
        p1_srch = self.browser.find_element(By.CSS_SELECTOR, '#tippy-18 > div > div > div > div > div > div > input')
        p1_srch.send_keys('Олема')
        p1_srch_res = self.browser.find_element(By.CSS_SELECTOR, '#tippy-18 > div > div > div > div > div > ul > li:nth-child(1)')
        p1_srch_res.click()


    def p2(self):
        p2 = self.browser.find_element(By.CSS_SELECTOR, '#ui-tab-a0a445a6 > div > div > div.calculation__bar.mb-4 > div > form > div:nth-child(1) > div:nth-child(2) > div > div > div.ui-select__content > div > div.ui-select__display.ui-select__display--with-icon')
        p2.click()
        p2_srch = self.browser.find_element(By.CSS_SELECTOR, '#tippy-19 > div > div > div > div > div > div > input')
        p2_srch.send_keys('Рочегда')
        p2_srch_res = self.browser.find_element(By.CSS_SELECTOR, '#tippy-19 > div > div > div > div > div > ul > li:nth-child(1)')
        p2_srch_res.click()


    def cargo(self):
        culture = self.browser.find_element(By.CSS_SELECTOR, '#ui-tab-a0a445a6 > div > div > div.calculation__bar.mb-4 > div > form > div:nth-child(1) > div.col-xs-12.col-sm-12.col-md-3.mb-4.mb-md-6 > div > div.ui-select__content > div > div.ui-select__display.ui-select__display--with-icon')
        culture.click()
        culture_type = self.browser.find_element(By.CSS_SELECTOR, '#tippy-20 > div > div > div > div > div > ul > li.ui-select-option.ui-select-option--type-basic.ui-select-option--size-normal.is-highlighted')
        culture_type.click()


    def weight(self):
        tones = self.browser.find_element(By.CSS_SELECTOR, '#ui-tab-a0a445a6 > div > div > div.calculation__bar.mb-4 > div > form > div:nth-child(1) > div:nth-child(4) > div > div.ui-textbox__content > label > input')
        tones.send_keys('200')


    def calculate(self):
        calc = self.browser.find_element(By.CSS_SELECTOR, '#ui-tab-a0a445a6 > div > div > div.calculation__bar.mb-4 > div > form > div:nth-child(2) > div.col-xs-12.col-md-3.d-md-flex.justify-content-md-end > button > div.ui-ripple-ink')
        calc.click()