from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopCart:
    def __init__(self, browser_variable):
        self.browser = browser_variable
        self.waiter = WebDriverWait(self.browser, 10)

    def get_cart(self):
        self.browser.get("https://www.saucedemo.com/cart.html")

        self.waiter.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="header_container"]//span[text()="Your Cart"]',
                )
            )
        )

    def press_checkout(self):
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
