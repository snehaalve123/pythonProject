import pytest
from POM.login import LoginPage
from tests import conftest
from time import sleep

class TestLogin:
    def test_login(self, driver):
        driver.get("https://demowebshop.tricentis.com/login")
        lp_obj = LoginPage(driver)
        lp_obj.enter_email()
        lp_obj.enter_pwd()
        lp_obj.click_login()
        sleep(5)

