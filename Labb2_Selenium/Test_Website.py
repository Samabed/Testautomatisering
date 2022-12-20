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
    search_results = driver.find_elements(By.XPATH, "//div[@class='search-results']")
    assert len(search_results) > 0


def test_check_product_price(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()

    # Hämta priset på produkten
    price_element = driver.find_element(By.XPATH, "//div[@class='price-current']")
    price = float(price_element.text.strip()[:-2].replace(',', '.'))

    # Kontrollera att priset är korrekt
    assert price == 450.00


def test_add_product_to_cart(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()
    webbhallen.add_product_to_cart()

    # Kontrollera att produkten finns i kundvagnen
    cart_items = driver.find_elements(By.XPATH, "//div[@class='cart-item']")
    assert len(cart_items) > 0


def test_go_to_cart(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_cart()

    # Kontrollera att kundvagnen öppnas och att den innehåller produkten som lades till
    cart_items = driver.find_elements(By.XPATH, "//div[@class='cart-item']")
    assert len(cart_items) > 0


def test_go_to_product_page(driver):
    webbhallen = Webbhallen(driver)
    webbhallen.go_to_product_page()

    # Kontrollera att produktsidan öppnas och att det finns en knapp för att lägga till produkten i kundvagnen
    add_to_cart_basket = driver.find_elements(By.XPATH, "//button[@id='add-product-to-cart']")
    assert len

    driver.close()




