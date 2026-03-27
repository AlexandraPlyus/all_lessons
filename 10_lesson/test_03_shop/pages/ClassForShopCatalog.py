import allure
from selenium.webdriver.common.by import By


class ShopCatalog:
    def __init__(self, browser_variable: str):
        """
        Функция принимает значение браузера
        """
        self.browser = browser_variable

    @allure.step("Добавление товары")
    def add_products(self):
        """
        Функция добавляет определённые товары в корзину
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        ).click()
