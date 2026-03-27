import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCart:

    def __init__(self, browser_variable: str):
        """
        Функция принимает значение браузера,
        и устанавливает ожидание 10 секунд
        """
        self.browser = browser_variable
        self.waiter = WebDriverWait(self.browser, 10)

    @allure.step("Переход в корзину")
    def get_cart(self):
        """
        Функция выполняет переход в корзину
        """
        self.browser.get("https://www.saucedemo.com/cart.html")

        self.waiter.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="header_container"]//span[text()="Your Cart"]',
                )
            )
        )

    @allure.step("Нажатие кнопки Checkout")
    def press_checkout(self):
        """
        Функция нажимает "Checkout"
        """
        self.browser.find_element(By.CSS_SELECTOR, "#checkout").click()

        self.waiter.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="header_container"]' +
                    '//span[text()="Checkout: Your Information"]',
                )
            )
        )
