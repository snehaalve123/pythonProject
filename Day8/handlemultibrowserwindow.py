import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM, Inc").click()

winhandles = driver.window_handles

driver.current_window_handle
handles = driver.window_handles
print(handles[0], handles[1])
driver.switch_to.window(handles[1])

for winhandle in winhandles:
    handle = driver.switch_to.window(winhandle)

    print(driver.title)

time.sleep(4)