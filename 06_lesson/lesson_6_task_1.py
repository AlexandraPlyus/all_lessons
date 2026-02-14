from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(browser, 16)

browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#content>p.bg-success"))
)

print(browser.find_element(By.CSS_SELECTOR, "#content>p.bg-success").text)
browser.quit()
