import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class Gv_Crt_Ordr:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    @allure.step("Заполнение поля 'Откуда' значением 'Олема'")
    def p1(self):
        with allure.step("Клик на поле 'Откуда'"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.ui-select__display")
            )).click()

        with allure.step("Ввод значения 'Олема' в поле поиска"):
            search_input = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tippy-1 > div > div > div > div > div > div > input")
            ))
            search_input.send_keys('Олема')

        with allure.step("Выбор пункта из выпадающего списка"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#tippy-1 > div > div > div > div > div > ul > li.ui-select-option.ui-select-option--type-basic.ui-select-option--size-normal.is-highlighted")
            )).click()

    @allure.step("Заполнение поля 'Куда' значением 'Рочегда'")
    def p2(self):
        with allure.step("Клик на поле 'Куда'"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "form > div:nth-child(1) > div:nth-child(2) div.ui-select__display")
            )).click()

        with allure.step("Ввод значения 'Рочегда' в поле поиска"):
            search_input = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tippy-2 > div > div > div > div > div > div > input")
            ))
            search_input.send_keys('Рочегда')

        with allure.step("Выбор первого пункта из выпадающего списка"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#tippy-2 > div > div > div > div > div > ul > li:nth-child(1)")
            )).click()

    @allure.step("Выбор культуры груза")
    def cargo(self):
        with allure.step("Открытие выпадающего списка культур"):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[1]/div[3]/div/div[2]/div/div[2]')
            )).click()

        with allure.step("Выбор первой культуры из списка"):
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#tippy-3 > div > div > div > div > div > ul > li.ui-select-option.ui-select-option--type-basic.ui-select-option--size-normal.is-highlighted")
            )).click()

    @allure.step("Ввод массы груза: 200 тонн")
    def weight(self):
        with allure.step("Заполнение поля массы значением 200"):
            weight_input = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[1]/div[4]/div/div[2]/label/input')
            ))
            weight_input.send_keys('200')

    @allure.step("Нажатие кнопки 'Рассчитать'")
    def calculate(self):
        with allure.step("Клик по кнопке рассчета"):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[2]/div[2]/button")
            )).click()

    @allure.step("Нажатие кнопки 'Продолжить'")
    def continue_order_creation(self):
        with allure.step('Клик по кнопке продолжения'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button/div[4]')
            )).click()

    # @allure.step('Ввод объёма макс.суточной отгрузки') -- Шаг на доработке
    # def insert_max_weight(self):
    #     with allure.step('Ввод значения макс.суточной отгрузки: 100тонн'):
    #         max_weight_input = self.wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[3]/div/div/div[1]/div/div/div[1]/label/input')
    #         ))
    #         max_weight_input.send_keys('100')

        # with allure.step('Клик на кнопку "Применить"'):
        #     self.wait.until(EC.element_to_be_clickable(
        #         (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[3]/div/div/div[1]/button/div[4]')
        #     )).click()

    @allure.step('Принятие условий договора')
    def accept_contract(self):
        with allure.step('Нажатие на чек-бокс договора'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[3]/div/div/div[3]/div/div/div[2]/div[4]/label')
            )).click()

    @allure.step('Ввод стоимости груза')
    def cargo_price_per_ton(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[4]/div/div[1]/div[2]/div/div[1]/label/input')
        )).send_keys('10')

    @allure.step('Ввод условий погрузки')
    def shipping_conditions(self):
        with allure.step('Ввод ограничений по высоте'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[5]/div/div[5]/div[2]/div/div[1]/label/input')
            )).send_keys('11')

        with allure.step('Указание способа погрузки'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[5]/div/div[6]/div[2]/div/div/div[1]/div')
            )).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div/div/div/div/ul/li[2]')
            )).click()

        with allure.step('Ввод номера контактного лица'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[5]/div/div[7]/div[2]/div/div/div/label/input')
            )).send_keys('Фейк Фейк Фейкович')

        with allure.step('Ввод номера телефона контактного лица'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/main/div[1]/form/div[5]/div/div[8]/div[2]/div/div/label/input')
            )).send_keys('77777777777')

    @allure.step('Публикация заказа')
    def publish(self):
        with allure.step('Нажатие на кнопку "Опубликовать"'):
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/button/div[4]')
            )).click()