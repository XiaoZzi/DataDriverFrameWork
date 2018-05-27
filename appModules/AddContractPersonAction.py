# -*- coding = utf-8 -*-
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time


class AddContractPerson(object):
    def __init__(self):
        print('add contract person')

    @staticmethod
    def add(d, contract_name, contract_mobile, contract_memo):
        try:
            # 创建主页实例对象
            hp = HomePage(d=d)
            # 单击通讯录按钮
            hp.addresslink().click()
            time.sleep(5)
            # 创建添加联系人实例对象
            apb = AddressBookPage(d=d)
            apb.create_contractperson_btn().click()
            apb.switch_to_frame()
            time.sleep(1)
            # 必填项
            apb.contract_person_name().send_keys(contract_name)
            # 必填项
            apb.contract_person_mobile().send_keys(contract_mobile)
            if contract_memo:
                # 非必填项
                apb.contract_person_email().send_keys(contract_memo)
            # 单击添加联系人页面确定按钮
            apb.save_contract_person().click()
        except Exception as e:
            # 打印堆栈异常信息
            print(traceback.print_exc())
            raise e


if __name__ == '__main__':
    # 打开
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.51kaihui.com/login/index')
    time.sleep(3)
    # 登录
    from appModules.LoginAction import LoginAction
    LoginAction.login(d=driver, username='18513510827', password='123456')
    time.sleep(3)
    # 新建联系人
    AddContractPerson.add(d=driver, contract_name=u'张三', contract_mobile='1234566788', contract_memo='')
    time.sleep(3)
    # 验证添加后张三在页面源码中
    assert u"张三" in driver.page_source
    driver.quit()