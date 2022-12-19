from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Webbhallen:
    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self):
        self.driver.get('https://www.webhallen.com/se/product/335143-Apple-AirTag-1-Pack')

    def search_for_product(self, product_name):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök bland över 16 000 produkter']")
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='search-results']")))

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[@id='add-product-to-cart']")
        add_to_cart_button.click()
