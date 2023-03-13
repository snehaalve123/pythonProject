import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
driver.maximize_window()
ac = ActionChains(driver)

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "(//*[name()='svg'][@role='presentation'])[2]").click()

userMgmt = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
Users = driver.find_element(By.XPATH, "(//a[normalize-space()='Users'])")
ac.move_to_element(userMgmt).move_to_element(Users).perform()

time.sleep(10)