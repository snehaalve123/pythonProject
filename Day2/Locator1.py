from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
'''
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.CLASS_NAME, "button-1").click()
'''
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Log").click()

driver.find_element(By.CLASS_NAME, "search-box-text").send_keys("Laptop")
driver.find_element(By.CLASS_NAME, "button-1").click()
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
print(type(links))
imgs = driver.find_elements(By.CLASS_NAME, "picture")
print(len(imgs))
print(type(imgs))

driver.find_element(By.CSS_SELECTOR(button.button-2)).click()
