import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.chrome(service = ser_obj)
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://www.facebook.com/")
driver.get("https://demo.nopcommerce.com/")

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
