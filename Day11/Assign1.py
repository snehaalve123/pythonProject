import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@ng-model = 'FirstName']").send_keys("mira")
driver.find_element(By.XPATH, "//div/input [@placeholder='Last Name']").send_keys("lad")
driver.find_element(By.XPATH, "//div/textarea[@ng-model ='Adress']").send_keys("address")
driver.find_element(By.XPATH, "//input[contains (@type, 'email')]").send_keys("adb@gmail.com")
driver.find_element(By.XPATH, "//input[starts-with (@type, 'tel')]").send_keys("9999098989")

driver.find_element(By.XPATH, "//input[contains (@value, 'Male')]").click()
checkboxes=driver.find_elements(By.XPATH, "//div[@class = 'col-md-4 col-xs-4 col-sm-4']/div/input[@type ='checkbox']")

for i in checkboxes:
    val = i.get_attribute('value')
    if val == "Cricket":
        i.click()
driver.find_element(By.XPATH, "//div[@id='msdd']").click()
time.sleep(5)
# drpdwn = Select(driver.find_elements(By.XPATH, "//div/ul[@style ='list-style:none;max-height: 230px;overflow: scroll;']"))
# for i in drpdwn:
#     print(i.get_attribute('value'))
# drpdwn.select_by_visible_text("Hindi")

drpdown = Select(driver.find_element(By.XPATH, "//select[@id ='Skills']"))
drpdown.select_by_visible_text("Python")

driver.find_element(By.XPATH, "//input[@id ='imagesrc']").send_keys("C:\\Users\\sneha\\Downloads\\img.png")
driver.execute_script("w")
driver.save_screenshot("C:\\Users\\sneha\\Downloads\\img.png")