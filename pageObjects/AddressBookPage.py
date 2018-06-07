# -*- coding = utf-8 -*-
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class AddressBookPage(object):
    def __init__(self, d):
        self.driver = d
        self.parseCF = ParseConfigFile()
        self.addContractOptions = self.parseCF.get_items_section("51kaihui_addContractsPage")

    def create_contractperson_btn(self):
        # 获取新建联系人按钮
        try:
            locate_type, locate_expression = \
                self.addContractOptions["addContractPage.createContractBtn".lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            raise e

    def switch_to_frame(self):
        # 跳转到新建联系人的弹窗
        try:
            locate_expression = self.addContractOptions["addContractPage.frame".lower()].split('>')[1]
            self.driver.switch_to.frame(locate_expression)
        except Exception as e:
            raise e

    def switch_to_default_frame(self):
        # 跳转到默认frame
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def contract_person_name(self):
        # 添加联系人时，弹窗上输入联系人姓名
        try:
            locate_type, locate_expression = \
                self.addContractOptions["addContractPage.contractPersonName".lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            raise e

    def contract_person_mobile(self):
        # 添加联系人时，弹窗上输入联系人电话
        try:
            locate_type, locate_expression = \
                self.addContractOptions["addContractPage.contractPersonMobile".lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            return e

    def contract_person_email(self):
        # 添加联系人时，弹窗上输入联系人邮箱
        try:
            locate_type, locate_expression = \
                self.addContractOptions["addContractPage.contractPersonEmail".lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            return e

    def save_contract_person(self):
        # 添加联系人时，弹窗上输入联系人邮箱
        try:
            locate_type, locate_expression = \
                self.addContractOptions["addContractPage.saveContractBtn".lower()].split('>')
            element_obj = get_element(d=self.driver, locate_type=locate_type, locate_expression=locate_expression)
            return element_obj
        except Exception as e:
            return e


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
    # 通讯录点击新建联系人
    add = AddressBookPage(d=driver)
    add.create_contractperson_btn().click()
    add.switch_to_frame()
    time.sleep(2)
    add.contract_person_name().send_keys('123')
    add.contract_person_mobile().send_keys('34')
    add.save_contract_person().click()
    add.switch_to_default_frame()
    time.sleep(3)
    driver.quit()