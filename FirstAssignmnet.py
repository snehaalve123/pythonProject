# TC1

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
ActualTitle = driver.title
ExpTitle = "Dashboard / nopCommerce administration"

if ActualTitle == ExpTitle:
    print("Login test passed")
else:
    print("Login test failed")
