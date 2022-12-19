class Webbhallen:
    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self):
        self.driver.get('https://www.webhallen.com/se/product/335143-Apple-AirTag-1-Pack')