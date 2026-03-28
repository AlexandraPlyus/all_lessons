from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPurchase:
    def __init__(self, browser_variable):
        self.browser = browser_variable
        self.browser.get("https://www.saucedemo.com/checkout-step-one.html")
        self.waiter = WebDriverWait(self.browser, 10)

    def insert_values(self, first_name, last_name, zip_code):
        self.browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys(
            first_name
        )
        self.browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(
            last_name
        )
        self.browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(
            zip_code
        )
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()

        self.waiter.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@id="header_container"]//' +
                    'span[text()="Checkout: Overview"]',
                )
            )
        )

    def total(self):
        return self.browser.find_element(
            By.CSS_SELECTOR,
            "#checkout_summary_container >" +
            "div >" +
            "div.summary_info >" +
            "div.summary_total_label",
        ).text
