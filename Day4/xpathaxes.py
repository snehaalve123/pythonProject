from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers")

# Self
txt = driver.find_element(By.XPATH, "//a[contains(text(),'Ambition Mica')]/self::a").text
print(txt)

# Parent
txt1 = driver.find_element(By.XPATH, "//a[contains(text(),'Ambition Mica')]/parent::td").text
print(txt1)

# Child
txt2 = driver.find_elements(By.XPATH, "//a[contains(text(),'Ambition Mica')]/ancestor::tr/child::td")
print(len(txt2))
for x in txt2:
    print(x.text)