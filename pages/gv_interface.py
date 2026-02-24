from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import gv_credentials

class Gv_Interface:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)  # Явное ожидание

    def open(self):
        self.browser.get('https://smartseeds.ru/profile')

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(4) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_notifications_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(5) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_eq_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_managers_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(2) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_shippings_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_shippings_calculation_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        )).click()

    def click_my_orders_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        )).click()

    def click_archive_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(3) > a > button > div.ui-ripple-ink')
        )).click()

    def eq_timeslots_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        )).click()

    def eq_registry_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(2) > a > button > div.ui-ripple-ink')
        )).click()

    def eq_my_shippers_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(3) > a > button > div.ui-ripple-ink')
        )).click()

    def eq_black_list_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(4) > a > button > div.ui-ripple-ink')
        )).click()

    def eq_journal_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(5) > a > button > div.ui-ripple-ink')
        )).click()