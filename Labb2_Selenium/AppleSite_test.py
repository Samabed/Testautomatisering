import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AppleSiteTest(unittest.TestCase):

    def setUp(self):
        # Create a new Chrome driver
        self.driver = webdriver.Chrome()

    def test_search_box_is_present(self):
        # Navigate to the Apple website
        self.driver.get("https://www.apple.com")

        # Check if the search box is present on the page
        self.assertTrue(self.is_element_present(By.ID, "ac-gn-link-search"))

    def tearDown(self):
        # Close the browser
        self.driver.close()

    def is_element_present(self):
        # Check if an element is present on the page
        try:
            self.driver.find_element(By.ID, value='ac-gn-link-search')
        except NoSuchElementException:
            return False
        return True


if __name__ == "__main__":
    unittest.main()

'''import self
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.apple.com/se/")
search_box = driver.find_element(By.ID, "ac-gn-link-search")
#assert "search" in driver.
self.assertTrue(self.is_element_present(By.ID, "ac-gn-link-search"))

search_box.send_keys("iPhone")
search_box.submit()
'''


