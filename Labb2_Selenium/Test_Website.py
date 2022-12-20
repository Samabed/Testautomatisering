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



