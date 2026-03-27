def test_calc_allure():

# """
# Тест проверяет работу калькулятора
# """


with allure.step("Открытие браузера"):
driver = http://webdriver.Chrome calculator_page = CalculatorPage(driver)
with allure.step("Открытие страницы калькулятора"):
http://calculator_page.open 
with allure.step("Установка задержки 45 секунд"):
calculator_page.set_delay(45)
with allure.step("Нажатие кнопки 7"):
http://calculator_page.click ("7")
with allure.step("Нажатие кнопки +"):
http://calculator_page.click or("+")
with allure.step("Нажатие кнопки 8"):
http://calculator_page.click ("8")
with allure.step("Нажатие кнопки ="):
http://calculator_page.click ()
with allure.step("Ожидание результата 15"):
calculator_page.wait_for_result(expected_result = "15")
with (allure.step("Проверка результата")):
actual_result = calculator_page.get_screen_text()

assert actual_result == "15"
with allure.step("Закрытие браузера"):
driver.quit()

@allure.title("Тестирование калькулятора: {num1} {operation} {num2} "
"= {expected_result}")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
