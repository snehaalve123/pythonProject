import pytest
from POM.register import RegisterPage
from tests import conftest


class TestRegister:
    def test_register(self, _driver):
        rp_obj = RegisterPage(_driver)
        rp_obj.select_gender()
        rp_obj.enter_fname()
        rp_obj.enter_lname()
        rp_obj.enter_pwd()
        rp_obj.enter_cpwd()
        rp_obj.enter_email()
        rp_obj.click_register()

    def test_register1(self, _driver):
        rp_obj = RegisterPage1(_driver)
        rp_obj.select_gender()
        rp_obj.enter_fname()
        rp_obj.enter_lname()
        rp_obj.enter_pwd()
        rp_obj.enter_cpwd()
        rp_obj.enter_email()
        rp_obj.click_register()

