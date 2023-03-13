import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.switch_to.frame("iframeResult")
button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
ac = ActionChains(driver)
ac.double_click(button).perform()
time.sleep(10)
stmt = driver.find_element(By.XPATH, "//p[@id='demo']").text
if stmt == "Hello World":
    print("test passed")
