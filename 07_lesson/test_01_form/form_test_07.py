from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from ClassFromForm import Form

red = "rgba(132, 32, 41, 1)"
green = "rgba(15, 81, 50, 1)"


def test_form():
    browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    form_exemplar = Form(browser)
    form_exemplar.insert_values("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
    form_exemplar.click_submit()

    assert form_exemplar.color_red() == red
    assert form_exemplar.color_green() == green

    browser.quit()
