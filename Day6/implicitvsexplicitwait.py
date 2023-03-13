from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.google.com/")
wait = WebDriverWait(driver,10)
#driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("Selenium")
driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
sel1 = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
sel1.click()
#driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()

