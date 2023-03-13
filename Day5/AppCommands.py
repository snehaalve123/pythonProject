# Application Commands

from selenium import webdriver

driver = webdriver.Chrome()

# Get URL
driver.get("https://demo.nopcommerce.com/")

# Get Current URL
print(driver.current_url)

# Get the page title
print(driver.title)

# Get the page source
print(driver.page_source)

# Close the browser
driver.quit()

