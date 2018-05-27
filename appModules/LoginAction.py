# -*- coding=utf-8 --
from pageObjects.LoginPage import LoginPage


class LoginAction(object):
    def __init__(self):
        print('login...')

    @staticmethod
    def login(d, username, password):
        try:
            login = LoginPage(d)
            login.username_obj().send_keys(username)
            login.password_obj().send_keys(password)
            login.login_button().click()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.51kaihui.com/login/index')
    import time
    time.sleep(3)
    LoginAction.login(d=driver, username='18513510827', password='123456')
    driver.quit()