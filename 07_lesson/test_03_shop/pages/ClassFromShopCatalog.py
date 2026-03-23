from selenium.webdriver.common.by import By

class ShopCatalog:
    def __init__(self, browser_variable):
        self.browser = browser_variable
        
    def add_products(self):
            self.browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
            self.browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
            self.browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()