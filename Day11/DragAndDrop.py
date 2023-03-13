import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
ac = ActionChains(driver)

driver.implicitly_wait(10)

Src_ele = driver.find_element(By.ID, "box5")
Trgt_ele = driver.find_element(By.ID, "box105")

ac.drag_and_drop(Src_ele, Trgt_ele).perform()

time.sleep(5)