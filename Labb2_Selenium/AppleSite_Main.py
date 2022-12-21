from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://www.apple.com/se/")
driver.implicitly_wait(10) #10 is in seconds
assert "Apple (Sverige)" in driver.title


# Locate the search input field
search_field = driver.find_element(By.XPATH, "/html/body/nav/div/ul[2]/li[12]/a")

driver.implicitly_wait(10) #10 is in seconds
# Enter the search query
search_field.send_keys("iPhone")




