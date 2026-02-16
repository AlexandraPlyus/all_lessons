import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    waiter = WebDriverWait(browser, 45)

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    browser.find_element(By.XPATH, "//div[@id='calculator']//span[@class='btn btn-outline-primary'][text()='7']").click()
    browser.find_element(By.XPATH, "//div[@id='calculator']//span[@class='operator btn btn-outline-success'][text()='+']").click()
    browser.find_element(By.XPATH, "//div[@id='calculator']//span[@class='btn btn-outline-primary'][text()='8']").click()
    browser.find_element(By.XPATH, "//div[@id='calculator']//span[@class='btn btn-outline-warning'][text()='=']").click()
    
    waiter.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
    )
    
    result = browser.find_element(By.CSS_SELECTOR, "#calculator > div.top > div.screen").text

    assert result == "15"
    browser.quit()
