import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_bye():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    waiter = WebDriverWait(browser, 10)

    browser.get("https://www.saucedemo.com/")

    usernames = browser.find_element(By.ID, "login_credentials").text.split("\n")
    username = usernames[1]

    password_for_all = browser.find_element(By.CLASS_NAME, "login_password").text.split("\n")
    password = password_for_all[1]

    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
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

    assert total == total_sum
    browser.quit()
