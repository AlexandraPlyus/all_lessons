import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

red = "rgba(132, 32, 41, 1)"
green = "rgba(15, 81, 50, 1)"

def test_form():
    browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    waiter = WebDriverWait(browser, 4)

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    browser.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys("")
    browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    waiter.until(
        EC.invisibility_of_element((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    assert browser.find_element(By.CSS_SELECTOR, '[id="zip-code"]').value_of_css_property("color") == red

    green_element_selectors = [
        "#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"
    ]
    
    for green_element in green_element_selectors:
        element = browser.find_element(By.CSS_SELECTOR, green_element)
        color_element = element.value_of_css_property("color")
        assert color_element == green

    browser.quit()
