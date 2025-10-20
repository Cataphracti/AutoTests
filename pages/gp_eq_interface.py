from selenium.webdriver.common.by import By

class EQ_interface:

    def __init__(self, browser):
        self.browser = browser

    def eq_choose_NZT(self):
        terminal_list = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__content > div.interior__body > div > div > div.scTerminal-content > div.scTerminal-options > div.d-flex.align-items-center.flex-wrap.mr-auto.scTerminal-option > div > div > div > div > div > div')
        terminal_list.click()
        nzt = self.browser.find_element(By.CLASS_NAME, 'ui-select-option__basic')
        nzt.click()