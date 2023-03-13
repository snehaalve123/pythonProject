import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
drp = driver.find_elements(By.XPATH,"//select[@id='speed']/option")
print(len(drp))
for i in drp:
    print(i.text)
    if i.text == "Fast":
        i.click()
time.sleep(3)

