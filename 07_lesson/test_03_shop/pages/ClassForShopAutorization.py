from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopAutorization:

    def __init__(self, browser_variable):
        self.browser = browser_variable
        self.browser.get("https://www.saucedemo.com/")
        self.waiter = WebDriverWait(self.browser, 10)

    def authorization(self):
        usernames = self.browser.find_element(
            By.ID, "login_credentials"
        ).text.split("\n")
        username = usernames[1]

        password_for_all = self.browser.find_element(
            By.CLASS_NAME, "login_password"
        ).text.split("\n")
        password = password_for_all[1]

        self.browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
            username
        )
        self.browser.find_element(By.CSS_SELECTOR, "#password").send_keys(
            password
        )
        self.browser.find_element(By.CSS_SELECTOR, "#login-button").click()

        self.waiter.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#react-burger-menu-btn")
            )
        )
