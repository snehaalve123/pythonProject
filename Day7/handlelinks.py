import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

# Click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
links = driver.find_elements(By.XPATH, "//a")
print(len(links))
for link in links:
    print(link.text)
time.sleep(5)
