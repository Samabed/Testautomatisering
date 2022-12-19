from Labb2_Selenium.Website import Webbhallen
from selenium.webdriver.common.by import By


def test_webbhallen(setup):
    webbhallen = Webbhallen(setup)

    # Go to the product page and search for a product
    webbhallen.go_to_product_page()
    webbhallen.search_for_product('335143')

    # Verify that the search results are displayed
    search_results = setup.find_elements(By.XPATH, "//p[@class='text-secondary']")
    assert "335143" in search_results

    # Add the product to the cart
    webbhallen.add_product_to_cart()

    # Navigate to the cart and verify that the product was added
    webbhallen.go_to_cart()
    cart_items = setup.find_elements(By.XPATH, "//div[@class='cart-items']/div")
    assert len(cart_items) > 0


class Testhallen:
    def test_item(self):
        artnr = Webbhallen(self.driver)
        artnr.findproduct("335143")
        artnr = self.driver.find_element(By.XPATH, "//p[@class='text-secondary']")
        artnr = artnr.text
        print(artnr)
        assert "335143" in artnr

    def test_namn(self):
        namn = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Apple AirTag - (1 Pack)'")
        namn = namn.text
        print(namn)
        assert "AirTag" in namn

    def test_price(self):
        price = self.driver.find_element(By.XPATH, "//div[@class='price-big']")
        price = price.text
        print(price)
        assert "450" in price

    def test_stock(self):
        stock = self.driver.find_element(By.XPATH, "//span[normalize-space()='I lager']")
        stock = stock.text
        print(stock)
        assert "Ej i lager" in stock


    def test_basket(self):
        basket = Webbhallen(self.driver)
        basket.basket()
        basket = self.driver.find_element(By.XPATH, "//div[@class='totalPriceRow']")
        basket = basket.text
        print(basket)
        assert "450" in basket

