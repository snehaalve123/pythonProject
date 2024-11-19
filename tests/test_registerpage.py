import pytest

from POM.login import LoginPage
from POM.register import RegisterPage
from tests import conftest
from time import sleep

class TestRegister:
    def test_register(self, driver):
        driver.get("https://demowebshop.tricentis.com/register")
        rp_obj = RegisterPage(driver)
        rp_obj.select_gender()
        rp_obj.enter_fname()
        rp_obj.enter_lname()
        rp_obj.enter_pwd()
        rp_obj.enter_cpwd()
        rp_obj.enter_email()
        rp_obj.click_register()
        sleep(5)

class TestLogin:
    def test_login(self, driver):
        driver.get("https://demowebshop.tricentis.com/login")
        lp_obj = LoginPage(driver)
        lp_obj.enter_email()
        lp_obj.enter_pwd()
        lp_obj.click_login()
        sleep(5)
