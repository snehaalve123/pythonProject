from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]").click()
ActualTitle = driver.title
ExpectedTitle = "OrangeHRM"
if ActualTitle == ExpectedTitle:
    print("login test passed")
else:
    print("login test failed")
driver.close()
