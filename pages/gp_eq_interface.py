from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EQ_interface:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def eq_choose_NZT(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior.interior--frame > div.interior__content > div.interior__body > div > div > div.scTerminal-content > div.scTerminal-options > div.d-flex.align-items-center.flex-wrap.mr-auto.scTerminal-option > div > div > div > div > div > div')
        )).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'ui-select-option__basic')
        )).click()