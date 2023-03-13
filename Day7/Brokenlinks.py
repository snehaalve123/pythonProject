# we need to install request package one-time activity

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests
driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
links = driver.find_elements(By.XPATH, "//a")
print(len(links))

for link in links:
    url = link.get_attribute('href')
    #print(url)
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print("This is a broken link:", url, res.status_code)
    else:
        print("This is a valid link:", url, res.status_code)

time.sleep(5)