from selenium.webdriver.common.by import By
from pages import gv_credentials

class Gv_Interface:

    def __init__(self, browser): ##Функция браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def open(self):
        self.browser.get('https://smartseeds.ru/profile') ##Открыть стр.профиля

    def click_profile_button(self): ##Открыть профиль
        profile_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(4) > div.menuSection__btn > a > button > div.ui-ripple-ink')  # Поиск элемента на странице
        profile_button.click()

    def click_notifications_button(self):
        notifications_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(5) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        notifications_button.click()

    def click_eq_button(self):
        eq_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        eq_button.click()

    def click_managers_button(self):
        managers_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(2) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        managers_button.click()

    def click_shippings_button(self):
        shippings_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__btn > a > button > div.ui-ripple-ink')
        shippings_button.click()

    def click_shippings_calculation_button(self):
        shippings_calculation_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        shippings_calculation_button.click()

    def click_my_orders_button(self):
        my_orders_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        my_orders_button.click()

    def click_archive_button(self):
        archive_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(1) > div.menuSection__children > div:nth-child(3) > a > button > div.ui-ripple-ink')
        archive_button.click()

    def eq_timeslots_button(self):
        timeslots_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(1) > a > button > div.ui-ripple-ink')
        timeslots_button.click()

    def eq_registry_button(self):
        registry_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(2) > a > button > div.ui-ripple-ink')
        registry_button.click()

    def eq_my_shippers_button(self):
        my_shippers_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(3) > a > button > div.ui-ripple-ink')
        my_shippers_button.click()

    def eq_black_list_button(self):
        black_list_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(4) > a > button > div.ui-ripple-ink')
        black_list_button.click()

    def eq_journal_button(self):
        journal_button = self.browser.find_element(By.CSS_SELECTOR, 'body > div.root > div.interior.interior--frame > div.interior__side.interior__side__hidden > div.interior__mobile-visibility > div > div.side__menu > div:nth-child(3) > div.menuSection__children > div:nth-child(5) > a > button > div.ui-ripple-ink')
        journal_button.click()