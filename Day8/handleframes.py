import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
parentFrame = driver.find_element(By.XPATH, "//iframe[@id='singleframe']")
driver.switch_to.frame(parentFrame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
time.sleep(5)
driver.switch_to.default_content()
driver.find_element(By.PARTIAL_LINK_TEXT, "Iframe with").click()

Frame1 = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(Frame1)
Frame2 = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(Frame2)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
time.sleep(5)