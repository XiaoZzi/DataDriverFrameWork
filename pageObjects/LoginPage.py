# -*- coding = utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class LoginPage(object):
    def __init__(self, d):
        self.driver = d
        self.parseCf = ParseConfigFile()
        self.loginOptions = self.parseCf.get_items_section('51kaihui_login')

    def username_obj(self):
        try:
            locate_type, locator_expression = self.loginOptions['loginPage.username'.lower()].split('>')
            element_obj = get_element(self.driver, locate_type=locate_type, locate_expression=locator_expression)
            return element_obj
        except Exception as e:
            raise e

    def password_obj(self):
        try:
            locate_type, locator_expression = self.loginOptions['loginPage.password'.lower()].split('>')
            element_obj = get_element(self.driver, locate_type=locate_type, locate_expression=locator_expression)
            return element_obj
        except Exception as e:
            raise e

    def login_button(self):
        try:
            locate_type, locator_expression = self.loginOptions['loginPage.loginbutton'.lower()].split('>')
            element_obj = get_element(self.driver, locate_type=locate_type, locate_expression=locator_expression)
            return element_obj
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.51kaihui.com/login/index')
    import time
    time.sleep(3)
    login = LoginPage(d=driver)
    login.username_obj().send_keys('18513510827')
    login.password_obj().send_keys('123456')
    login.login_button().click()
    time.sleep(3)
    driver.quit()