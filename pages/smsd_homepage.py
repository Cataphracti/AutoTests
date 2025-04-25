import time

from selenium.webdriver.common.by import By

class SMSDHomePage: ##Сущность домашней страницы сайта с описанными функциями и готовыми действиями для тестов

    def __init__(self, browser): ##Функция браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def open(self):
        self.browser.get('https://smartseeds.ru/') ##Открыть домашнюю стр.сайта

    def click_authorize_button(self):
        authorize_button = self.browser.find_element(By.XPATH, '//*[@id="layout"]/header/div/div[1]/div[3]/div[4]/div/button') #Поиск элемента на странице
        authorize_button.click()
