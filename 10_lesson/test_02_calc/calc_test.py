import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ClassForCalc import Calc

"""
Тестирование работы задержки калькулятора
"""


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы задержки")
@allure.feature("Задержка")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():

    with allure.step("Настройка работы браузера"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        calc_exemplar = Calc(browser)

    calc_exemplar.insert_value_delay("45")

    calc_exemplar.press_the_button("7")
    calc_exemplar.press_the_button("+")
    calc_exemplar.press_the_button("8")
    calc_exemplar.press_the_button("=")

    with allure.step("Проверка результата"):
        assert calc_exemplar.result() == "15"

    with allure.step("Закрытие браузера"):
        browser.quit()
