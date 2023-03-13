import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alertwindow = driver.switch_to.alert
alertwindow.text
alertwindow.send_keys("welcome")
alertwindow.accept()
time.sleep(4)
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alertwindow = driver.switch_to.alert
alertwindow.dismiss()
time.sleep(4)

