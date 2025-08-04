from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Gv_Crt_Ordr:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def p1(self):
        # Клик на поле "Откуда"
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.ui-select__display")
        )).click()

        # Ввод и выбор пункта
        search_input = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#tippy-1 > div > div > div > div > div > div > input")
        ))
        search_input.send_keys('Олема')

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tippy-1 > div > div > div > div > div > ul > li.ui-select-option.ui-select-option--type-basic.ui-select-option--size-normal.is-highlighted")
        )).click()

    def p2(self):
        # Аналогично для поля "Куда"
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "form > div:nth-child(1) > div:nth-child(2) div.ui-select__display")
        )).click()

        search_input = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#tippy-2 > div > div > div > div > div > div > input")
        ))
        search_input.send_keys('Рочегда')

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#tippy-2 > div > div > div > div > div > ul > li:nth-child(1)")
        )).click()

    def cargo(self):
        # Выбор культуры
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[1]/div[3]/div/div[2]/div/div[2]/span")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div/div/div/div/div/ul/li[1]/div")
        )).click()

    def weight(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[1]/div[4]/div/div[2]/label/input')
        )).send_keys('200')

    def calculate(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/form/div[2]/div[2]/button/div[4]")
        )).click()