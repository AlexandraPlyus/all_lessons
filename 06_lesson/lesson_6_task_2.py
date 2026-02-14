from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")
sleep(1) # sleep использую для наглядности про воспроизведении

browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
sleep(1)

updating_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")
updating_button.click()
sleep(1)

print(updating_button.text)
browser.quit()
