# -*-coding=utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class EditContracts(object):
    def __init__(self, d):
        self.driver = d
        self.parseCF = ParseConfigFile()
        self.editContract = self.parseCF.get_items_section('51kaihui_editContractsMessagePage')

    def contract_table(self):
        try:
            locate_type, locate_expression = \
                self.editContract['editContractsMessagePage.table'.lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type,
                                      locate_expression=locate_expression)
            print(locate_type, locate_expression)
            return element_obj
        except Exception as e:
            raise e

    def contract_table_rows(self):
        try:
            locate_type, locate_expression = \
                self.editContract['editContractsMessagePage.tableRows'.lower()].split('>')
            element_obj = get_elements(d=self.driver, locate_type=locate_type,
                                       locate_expression=locate_expression)
            print(element_obj)
            return element_obj
        except Exception as e:
            raise e

    def contract_table_cols(self):
        try:
            locate_type, locate_expression = \
                self.editContract['editContractsMessagePage.tableCols'.lower()].split('>')
            element_obj = get_elements(d=self.driver,
                                       locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # 打开
    driver.get('https://www.51kaihui.com/login/index')
    import time
    time.sleep(3)
    # 登录
    from appModules.LoginAction import LoginAction
    LoginAction.login(d=driver, username='18513510827', password='123456')
    time.sleep(5)
    # 主页点击通讯录
    from pageObjects.HomePage import HomePage
    address = HomePage(d=driver)
    address.addresslink().click()
    time.sleep(5)
    # 删除用户
    # table = driver.find_element_by_id('mtg-activity-table')
    # print(len(table.find_elements_by_tag_name('tr')))
    a = EditContracts(d=driver)
    table = a.contract_table()
    print('table_rows:', len(table.contract_table_rows()))
    time.sleep(3)
    driver.quit()
