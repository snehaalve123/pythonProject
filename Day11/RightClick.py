import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://demo.automationtesting.in/Register.html")
button = driver.find_element(By.XPATH, "//textarea[@class='form-control ng-pristine ng-untouched ng-valid']")

ac = ActionChains(driver)
ac.context_click(button).perform()

time.sleep(10)