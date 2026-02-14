from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(browser, 10)

browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)
sleep(1)

div = browser.find_element(By.CSS_SELECTOR, "#image-container")
img = div.find_elements(By.CSS_SELECTOR, "img")
img_3 = img[2]
src = img_3.get_attribute("src")

print(src)
browser.quit()
