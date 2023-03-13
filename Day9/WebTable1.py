from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Program Files\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
NoOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
NoOfCols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))

print(NoOfRows, NoOfCols)

# # Retrive all data
# for r in range(2,NoOfRows+1):
#     for c in range(1, NoOfCols):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='    ')
#     print()

# Retrive specific data
for r in range(2,NoOfRows+1):
    AuthorName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if AuthorName == "Mukesh":
        BookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        Price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(AuthorName, "   ", BookName, "   ", Price)

