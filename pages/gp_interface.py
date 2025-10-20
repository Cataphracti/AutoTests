from selenium.webdriver.common.by import By
from pages import gv_credentials

class Gp_Interface:

    def __init__(self, browser): ##Функция браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def open(self):
        self.browser.get('https://smartseeds.ru/profile') ##Открыть стр.профиля

    def click_orders_search_button(self):
        orders_search_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        orders_search_button.click()

    def click_my_orders_button(self):
        my_orders_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(2) > a > button > div.ui-ripple-ink')
        my_orders_button.click()

    def click_drivers_button(self):
        drivers_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        drivers_button.click()

    def click_vehicles_button(self):
        vehicles_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(4) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        vehicles_button.click()

    def click_trailers_button(self):
        trailers_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(5) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        trailers_button.click()

    def click_finance_button(self):
        finance_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(6) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        finance_button.click()

    def click_bonus_program_button(self):
        bonus_program_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(7) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        bonus_program_button.click()

    def click_profile_button(self):
        profile_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(8) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        profile_button.click()

    def click_notifications_button(self):
        notifications_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(9) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        notifications_button.click()

    def close_reminder_popup(self):
        close_button = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div/div/div/div/div[3]/button[1]/div[4]')
        close_button.click()

    def click_eq_button(self):
        eq_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(2) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        eq_button.click()