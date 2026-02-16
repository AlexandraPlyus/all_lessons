from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

updating_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")
updating_button.click()

print(updating_button.text)
browser.quit()
