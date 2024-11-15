from data import reading_objects
from selenium import webdriver
from library.page_wrapper import PageWrapper

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()

reading_locator_obj = reading_objects.reading_locators()


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_wrapper_obj = PageWrapper(driver)

    def select_gender(self):
        self.page_wrapper_obj.click_button(reading_locator_obj['radio_gender'])

    def enter_fname(self):
        # self.driver.find_element(*reading_locator_obj['txt_fname']).send_keys('peter')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_fname'], 'peter')

    def enter_lname(self):
        # driver.find_element(*reading_locator_obj['txt_lname']).send_keys('jade')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_lname'], 'jade')

    def enter_email(self):
        # driver.find_element(*reading_locator_obj['txt_email']).send_keys('peter.jade@gmail.com')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_email'], 'peter.jade@gmail.com')

    def enter_pwd(self):
        # driver.find_element(*reading_locator_obj['txt_pwd']).send_keys('Peter@123')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_pwd'], 'peter@123')

    def enter_cpwd(self):
        # driver.find_element(*reading_locator_obj['txt_cpwd']).send_keys('Peter@123')
        self.page_wrapper_obj.enter_text(reading_locator_obj['txt_cpwd'], 'Peter@123')

    def click_register(self):
        # driver.find_element(*reading_locator_obj['btn_register']).click()
        self.page_wrapper_obj.click_button(reading_locator_obj['btn_register'])

# rp_obj = RegisterPage(driver)
# rp_obj.select_gender()
# rp_obj.enter_fname()
# rp_obj.enter_lname()
# rp_obj.enter_pwd()
# rp_obj.enter_cpwd()
# rp_obj.enter_email()
# rp_obj.click_register()
