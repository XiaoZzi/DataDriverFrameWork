# -*- coding = utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class HomePage(object):
    def __init__(self, d):
        self.driver = d
        self.parseCF = ParseConfigFile()

    def addresslink(self):
        try:
            # 从定位表达式配置文件中读取定位通讯录按钮的定位方式和表达式
            locate_type, locate_expression = \
                self.parseCF.get_option_value('51kaihui_homePage', 'homePage.addressbook').split(">")
            element_obj = get_element(self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.51kaihui.com/login/index')
    import time
    time.sleep(3)
    from appModules.LoginAction import LoginAction
    LoginAction.login(d=driver, username='18513510827', password='123456')
    time.sleep(5)
    address = HomePage(d=driver)
    address.addresslink().click()
    driver.quit()