from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

search = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/input")
search.clear()
search.send_keys("Sky")
sleep(1) # Чтобы было видно "Sky"

search.clear()
search.send_keys("Pro")

driver.quit()
