import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:

    @allure.step("Создание экземпляра класса от указанного браузера")
    def __init__(self, browser_value: str):
        """
        Функция принимает значение браузера,
        и устанавливает ожидание 45 секунд
        """
        self.browser = browser_value
        self.browser.get(
            "https:" +
            "//bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.waiter = WebDriverWait(self.browser, 45)

    @allure.step("Установка задержки {value}")
    def insert_value_delay(self, value: int):
        """
        Подставляет полученное значение в поле задержки
        """
        self.browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    @allure.step("Нажатие кнопки {button}")
    def press_the_button(self, button: str):
        """
        Функция принимает значения и
        нажимает на соответствующие кнопки на калькуляторе
        """
        if button == "0":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='0']",
            ).click()
        elif button == "1":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='1']",
            ).click()
        elif button == "2":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='2']",
            ).click()
        elif button == "3":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='3']",
            ).click()
        elif button == "4":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='4']",
            ).click()
        elif button == "5":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='5']",
            ).click()
        elif button == "6":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='6']",
            ).click()
        elif button == "7":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='7']",
            ).click()
        elif button == "8":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='8']",
            ).click()
        elif button == "9":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='9']",
            ).click()
        elif button == ".":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-primary'][text()='.']",
            ).click()
        elif button == "+":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='operator btn btn-outline-success']" +
                "[text()='+']",
            ).click()
        elif button == "-":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='operator btn btn-outline-success']" +
                "[text()='-']",
            ).click()
        elif button == "÷":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='operator btn btn-outline-success']" +
                "[text()='÷']",
            ).click()
        elif button == "x":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='operator btn btn-outline-success']" +
                "[text()='x']",
            ).click()
        elif button == "=":
            self.browser.find_element(
                By.XPATH,
                "//div[@id='calculator']" +
                "//span[@class='btn btn-outline-warning'][text()='=']",
            ).click()
        else:
            print(button + " - Нет такой кнопки")

        self.waiter.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
        )

    def result(self) -> float:
        """
        Функция возвращает ответ калькулятора
        """
        return self.browser.find_element(
            By.CSS_SELECTOR, "#calculator > div.top > div.screen"
        ).text
