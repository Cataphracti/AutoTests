from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import gv_credentials

class Gp_Interface:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 2)

    def open(self):
        self.browser.get('https://smartseeds.ru/profile')

    def click_orders_search_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        )).click()

    def click_my_orders_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(2) > a > button > div.ui-ripple-ink')
        )).click()

    def click_drivers_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_vehicles_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(4) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_trailers_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(5) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_finance_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(6) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_bonus_program_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(7) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(8) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def click_notifications_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(10) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()

    def close_reminder_popup(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div[4]/div/div/div/div/div[3]/button[1]/div[4]')
        )).click()

    def click_eq_button(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#app > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(2) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        )).click()