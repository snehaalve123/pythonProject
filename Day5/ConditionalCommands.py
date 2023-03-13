# Conditional Commands

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# is_displayed and is_enabled
searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Search box is displayed...", searchbox.is_displayed()) # True
print("Search box is enabled...", searchbox.is_enabled()) # True

# is_selected
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default radio box status...")
print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #False

rd_male.click()
print("After enabling male radio box status...")
print(rd_male.is_selected()) #True
print(rd_female.is_selected()) #False

rd_female.click()
print("After enabling female radio box status...")
print(rd_male.is_selected()) #False
print(rd_female.is_selected()) #True



