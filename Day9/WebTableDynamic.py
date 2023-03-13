import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()


driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//ul[@role='menu']//li").click()

rows = driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[5]")
crows = len(rows)
count = 0
for row in rows:
    if row.text == "Enabled":
        UserName = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+str(count+1)+"]/div/div[3]/div").text
        print(UserName,row.text)

    else:
        UserName = driver.find_element(By.XPATH,
                                       "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[" + str(
                                           count + 1) + "]/div/div[3]/div").text
        print(UserName, row.text)
    count = +1
time.sleep(5)
print("No of enabled users:", count)
print("No of disabled users", crows-count)


