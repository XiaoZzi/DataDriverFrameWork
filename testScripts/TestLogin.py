# -*- coding=utf-8 -*-
from selenium import webdriver
from appModules.LoginAction import LoginAction
import time


def test_login():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.51kaihui.com/login/index')
        time.sleep(3)
        LoginAction.login(d=driver, username='18513510827', password='123456')
        time.sleep(3)
    except Exception as e:
        raise e


if __name__ == '__main__':
    test_login()
    print(u'登录成功')