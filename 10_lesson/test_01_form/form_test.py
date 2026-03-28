import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager

from ClassForForm import Form

red = "rgba(132, 32, 41, 1)"
green = "rgba(15, 81, 50, 1)"


@allure.title("Изменения цвета полей")
@allure.description(
    "Тест на изменения цвета полей при внесении валидных и невалидных данных"
)
@allure.feature("Изменения")
@allure.severity(allure.severity_level.NORMAL)
def test_form():

    with allure.step("Настройка работы браузера"):
        browser = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
            )

        form_exemplar = Form(browser)

    form_exemplar.insert_values(
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "test@skypro.com",
        "+7985899998787",
        "",
        "Москва",
        "Россия",
        "QA",
        "SkyPro",
    )
    form_exemplar.click_submit()

    with allure.step("Проверка поля с невалидными данными"):
        assert form_exemplar.color_red() == red

    with allure.step("Проверка поля с валидными данными"):
        assert form_exemplar.color_green() == green

    with allure.step("Закрытие браузера"):
        browser.quit()
