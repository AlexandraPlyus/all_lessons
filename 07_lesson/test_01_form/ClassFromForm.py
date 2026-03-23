from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Form:

    def __init__(self, driver_value):
        self.browser = driver_value
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.waiter = WebDriverWait(self.browser, 10)

    def insert_values(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.browser.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)
        self.browser.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self.browser.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
        self.browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self.browser.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(zip_code)
        self.browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self.browser.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
        self.browser.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)
        self.browser.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def click_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        self.waiter.until(
        EC.invisibility_of_element((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
        
    def color_red(self):
        return str(self.browser.find_element(By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property("color"))

    def color_green(self):
        green_element_selectors = [
            "#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"
        ]
    
        for green_element in green_element_selectors:
            return str(self.browser.find_element(By.CSS_SELECTOR, green_element).value_of_css_property("color"))
