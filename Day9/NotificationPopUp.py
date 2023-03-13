from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
ops = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser_obj)
#ops.add_argument("--disable-notification")

driver.get("https://whatmyloacation.com/")