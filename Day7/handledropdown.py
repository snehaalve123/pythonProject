import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.geodatasource.com/software/country-region-dropdown-menu-demo")

all_drp = driver.find_element(By.XPATH, "//select[@country-data-region-id='gds-cr-one']")
allopt = Select(all_drp)
# allopt.select_by_visible_text("India")
# time.sleep(4)
# allopt.select_by_index(4) # Albania
# time.sleep(4)
# allopt.select_by_value("Colombia")
# time.sleep(4)

opt = allopt.options
print(len(opt))

# for op in opt:
#     print(op.text)
for op in opt:
    if op.text == "India":
        op.click()
time.sleep(4)

