from selenium.webdriver.common.by import By

class HomePage: ##Сущность домашней страницы сайта с описанными функциями и готовыми действиями для тестов

    def __init__(self, browser): ##Объявление функции браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html') ##Открыть домашнюю стр.сайта

    def click_galaxy_s6(self): ##Действия нажатия на элемент
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')##Поиск элемента на странице
        galaxy_s6.click() ##Само нажатие

    def click_monitor(self): ##Действия нажатия на элемент
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')##Поиск элемента на странице
        monitor_link.click()##Само нажатие

    def check_products_count(self, count): ##Проверка кол-ва карточек товаров на целевой странице
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')##Поиск элемента на странице (по классу)
        assert len(monitors) == count ##Ожидаемый результат (count это переменная которая отвечает за то, какое кол-во карточек ожидаем)
