from selenium.webdriver.common.by import By

class ProductPage: ##Сущность страницы с мониторами с описанными функциями и готовыми действиями для тестов

    def __init__(self, browser): ##Объявление функции браузера через который будут открываться стр. и осуществляться действия
        self.browser = browser

    def check_title_is(self, title):
            page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2') ##Поиск элемента на странице
            assert page_title.text == title ##Ожидаемый результат (ждём, что у стр. есть заголовок)