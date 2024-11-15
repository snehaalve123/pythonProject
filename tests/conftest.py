import pytest
from selenium import webdriver


@pytest.fixture()
def _driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)

    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()

    yield driver
    driver.quit()