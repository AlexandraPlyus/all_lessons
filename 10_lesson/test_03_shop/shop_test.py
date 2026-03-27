import allure
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.ClassForShopAutorization import ShopAutorization
from pages.ClassForShopCatalog import ShopCatalog
from pages.ClassForShopCart import ShopCart
from pages.ClassForShopPurchase import ShopPurchase


@allure.title("Оформление покупки")
@allure.description(
    "Тест проверяет добавление товаров в корзину" +
    "и получившуюся итоговую стоимость"
    )
@allure.feature("Сумма в корзине")
@allure.severity(allure.severity_level.CRITICAL)
def test_bye():

    with allure.step("Настройка работы браузера"):
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
            )
        shop_autorization_exemplar = ShopAutorization(browser)

    shop_autorization_exemplar.authorization()

    shop_catalog_exemplar = ShopCatalog(browser)
    shop_catalog_exemplar.add_products()

    shop_cart_exemplar = ShopCart(browser)
    shop_cart_exemplar.get_cart()
    shop_cart_exemplar.press_checkout()

    shop_purchase_exemplar = ShopPurchase(browser)
    shop_purchase_exemplar.insert_values(
        "Иван",
        "Петров",
        "101135"
    )

    total_sum = "Total: $58.29"

    with allure.step("Сравнение фактической стоимости с ожидаемой"):
        assert shop_purchase_exemplar.total() == total_sum

    browser.quit()
