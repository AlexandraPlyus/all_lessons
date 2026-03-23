import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ClassFromCalc import Calc

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calc_exemplar = Calc(browser)
    calc_exemplar.insert_value_delay("45")

    calc_exemplar.press_the_button("7")
    calc_exemplar.press_the_button("+")
    calc_exemplar.press_the_button("8")
    calc_exemplar.press_the_button("=")
    
    assert calc_exemplar.result() == "15"
    browser.quit()