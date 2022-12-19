import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Skapar en webdriver-instans
    driver = webdriver.Chrome()
    yield driver

