import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_bye():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    waiter = WebDriverWait(browser, 4)

    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()

    waiter.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#react-burger-menu-btn"))
    )

    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a[data-test='shopping-cart-link']").click()

    waiter.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header_container"]//span[text()="Your Cart"]'))
    )

    browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    waiter.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header_container"]//span[text()="Checkout: Your Information"]'))
    )
    
    browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys("имя")
    browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys("фамилия")
    browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("676 767")
    browser.find_element(By.CSS_SELECTOR, "#continue").click()

    waiter.until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="header_container"]//span[text()="Checkout: Overview"]'))
    )

    total = browser.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text
    total_sum = "Total: $58.29"
    browser.quit()
    
    assert total == total_sum
