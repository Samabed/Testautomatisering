import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Labb2_Selenium.Website import Webbhallen


@pytest.fixture
def driver():
    # Skapar en webdriver-instans
    driver = webdriver.Chrome()
    yield driver


def test_search_for_product(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()
    webbhallen.search_for_product('Apple AirTag')

    # Kontrollera att sökresultatet visas på sidan
    search_results = driver.find_elements(By.XPATH, "//p[@class='text-secondary']")
    assert "335143" in search_results


def test_check_product_price(driver, price=450):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()

    # Hämta priset på produkten
    price_element = driver.find_element(By.XPATH, "//div[@id='add-product-to-cart']")

    # Kontrollera att priset är korrekt
    assert price == 450.00 in price_element


def test_add_product_to_cart(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()
    webbhallen.add_product_to_cart()

    # Kontrollera att produkten finns i kundvagnen
    cart_items = driver.find_elements(By.XPATH, "//div[@class='cart-counter']")
    assert len(cart_items) == 1


def test_go_to_cart(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_cart()

    # Kontrollera att kundvagnen öppnas och att den innehåller produkten som lades till
    cart_items = driver.find_elements(By.XPATH, "//div[@class='input-number _tiny hide-spinner")
    assert len(cart_items) > 0


def test_go_to_product_page(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()

    # Kontrollera att totalsumma stämmer med produkten
    add_to_cart_basket = driver.find_elements(By.XPATH, "//div[@class='cart-total']")
    assert "450.00" in add_to_cart_basket

    driver.close()




