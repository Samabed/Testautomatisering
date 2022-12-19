from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Webbhallen:
    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self):
        self.driver.get('https://www.webhallen.com/se/product/335143-Apple-AirTag-1-Pack')

    def search_for_product(self, product_name):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök bland över 16 000 produkter']")
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)