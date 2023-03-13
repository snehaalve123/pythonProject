import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

# Locator matching with single element
ele = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
ele.send_keys()

# Locator matching with multiple elements
ele = driver.find_element(By.XPATH, "//div[@class='footer-upper']/following::div")
print(ele.text)

# Element not available then NoSuchElementException
# Login_ele = driver.find_element(By.LINK_TEXT, "LOG")
# Login_ele.click()

#### findelements returns multiple elements

#  Locator matching with single web element
eles = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(eles))
eles[0].send_keys("Laptop")
time.sleep(5)

#  Locator matching with multiple web elements
eles = driver.find_elements(By.XPATH, "//div[@class='footer-upper']/following::div")
print(len(eles))
for ele in eles:
    print(ele.text)
time.sleep(5)

# text vs get_attribute
login = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("login text using text:", login.text) #Log in
print("login text using get attribute:", login.get_attribute('value'))

email = driver.find_element(By.XPATH, "//*[@id='Email']")
email.send_keys("abc@gmail.com")
print("login text using text:", email.text)
print("login text using get attribute:", email.get_attribute('value')) #abc@gmail.com

time.sleep(5)
