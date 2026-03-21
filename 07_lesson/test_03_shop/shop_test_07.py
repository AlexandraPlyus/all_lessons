import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.ClassFromShopAutorization import ShopAutorization
from pages.ClassFromShopCatalog import ShopCatalog
from pages.ClassFromShopCart import ShopCart
from pages.ClassFromShopPurchase import ShopPurchase

def test_bye():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    shop_autorization_exemplar = ShopAutorization(browser)
    shop_autorization_exemplar.authorization()
    
    shop_catalog_exemplar = ShopCatalog(browser)
    shop_catalog_exemplar.add_products()

    shop_cart_exemplar = ShopCart(browser)
    shop_cart_exemplar.get_cart()
    shop_cart_exemplar.press_checkout()

    shop_purchase_exemplar = ShopPurchase(browser)
    shop_purchase_exemplar.insert_values("Иван", "Петров", "101135")

    total_sum = "Total: $58.29"
    assert shop_purchase_exemplar.total() == total_sum

    browser.quit()
