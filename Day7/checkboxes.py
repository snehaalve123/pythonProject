import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a").click()
time.sleep(5)
checkboxes = driver.find_elements(By.XPATH, "(//input[contains(@name,'checkbox_products')]) ")
print(len(checkboxes))

for checkbox in checkboxes:
    #checkbox.click()
    val=checkbox.get_attribute('Value')
    print(val)
    if val == "1" or val == "10":
        checkbox.click()
        print("---")

time.sleep(15)