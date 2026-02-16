from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, ".fa").click()

logget = driver.find_element(By.CSS_SELECTOR, '#flash').text

print(logget)
driver.quit()
