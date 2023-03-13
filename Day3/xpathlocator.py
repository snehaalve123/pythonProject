from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# Absolute XPATH
'''
driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/input[1]").send_keys("selenium")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]").click()

# Relative XPATH
driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("sele")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# OR
driver.find_element(By.XPATH, "//input[@id='small-searchterms' or @placeholder='Search store']").send_keys("Laptop")
# AND
driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button' and @type='submit']").click()
'''

# Contains and Starts with and text()

driver.find_element(By.XPATH, "//input[contains(@class,'search')]").send_keys("Laptop")
driver.find_element(By.XPATH, "//button[starts-with(@class, 'button-1 search')]").click()
driver.find_element(By.XPATH, "//a[text()='Asus N551JK-XO076H Laptop']").click()

driver.implicitly_wait(5)

