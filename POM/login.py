from data import reading_objects
from library.page_wrapper import PageWrapper

reading_locator_obj = reading_objects.reading_locators()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_wrapper_obj = PageWrapper(driver)

    def enter_email(self):
        # self.driver.find_element(*reading_locator_obj['txt_fname']).send_keys('peter')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_lemail'], 'peter.jade@gmail.com')

    def enter_pwd(self):
        # driver.find_element(*reading_locator_obj['txt_pwd']).send_keys('Peter@123')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_pwd1'], 'Peter@123')

    def click_login(self):
        # driver.find_element(*reading_locator_obj['btn_register']).click()
        self.page_wrapper_obj.click_button(reading_locator_obj['btn_login'])


