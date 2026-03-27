import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Form:

    @allure.step("Создание экземпляра класса от указанного браузера")
    def __init__(self, driver_value: str):
        """
        Функция принимает значение браузера,
        и устанавливает ожидание 10 секунд
        """
        self.browser = driver_value
        self.browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self.waiter = WebDriverWait(self.browser, 10)

    @allure.step("Внесение значений")
    def insert_values(
        self,
        first_name: str,
        last_name: str,
        address: str,
        email: str,
        phone: str,
        zip_code: str,
        city: str,
        country: str,
        job_position: str,
        company: str,
    ):
        """
        Функция берёт значения и заполняет ими поля по порядку
        """
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="first-name"]'
        ).send_keys(first_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="last-name"]'
        ).send_keys(last_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="address"]'
        ).send_keys(address)
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]'
        ).send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(
            phone
        )
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]'
        ).send_keys(zip_code)
        self.browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(
            city
        )
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="country"]'
        ).send_keys(country)
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="job-position"]'
        ).send_keys(job_position)
        self.browser.find_element(
            By.CSS_SELECTOR, '[name="company"]'
        ).send_keys(company)

    @allure.step("Нажатие кнопки Submit")
    def click_submit(self):
        """
        Функция нажимает на кнопу "Submit"
        """
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

        self.waiter.until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, 'button[type="submit"]')
            )
        )

    def color_red(self) -> str:
        """
        Функция находит по id поле которое должно стать красным
        и возвращает его фактический цвет
        """
        return str(
            self.browser.find_element(
                By.CSS_SELECTOR, '[id="zip-code"]'
            ).value_of_css_property("color")
        )

    def color_green(self) -> str:
        """
        Функция находит по id поля которые должны стать зелёными
        и возвращает их фактический цвет
        """
        green_element_selectors = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company",
        ]

        for green_element in green_element_selectors:
            return str(
                self.browser.find_element(
                    By.CSS_SELECTOR, green_element
                ).value_of_css_property("color")
            )
