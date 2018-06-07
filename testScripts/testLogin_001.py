# -*- coding=utf-8 -*-
from selenium import webdriver
from appModules.LoginAction import LoginAction
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
import time
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.excelObj = ParseExcel()
        self.excelObj.load_workbook(dataFilePath001)

    def tearDown(self):
        pass

    def test_login(self):
        logging.info(u'登录测试用例现在开始执行')
        try:
            user_sheet = self.excelObj.get_sheetbyname(u'login')
            is_execute = self.excelObj.get_column(user_sheet, login_isExecute)
            logging.debug('is_execute[1:]:%s' % is_execute[1:])
            for idx, value in enumerate(is_execute[1:]):
                if value == 'y':
                    user_data = self.excelObj.get_row(user_sheet, idx+2)
                    username = user_data[login_username - 1]
                    password = user_data[login_password - 1]
                    assert_word = user_data[login_assert - 1]
                    driver = webdriver.Chrome()
                    driver.get('https://www.51kaihui.com/login/index')
                    time.sleep(3)
                    LoginAction.login(d=driver, username=username, password=password)
                    logging.info(u'登录用户名:%s,密码:%s' % (username, password))
                    time.sleep(3)
                    try:
                        assert assert_word in driver.page_source
                    except AssertionError as e:
                        logging.info(u'用户%s断言关键字:%s，断言失败' % (username, assert_word))
                        self.excelObj.write_cell(sheet=user_sheet,
                                                 content='failed',
                                                 row_number=idx+2,
                                                 column_number=login_testResult,
                                                 style='red')
                        self.excelObj.write_cell_currenttime(user_sheet, row_number=idx+2, column_number=login_testTime)
                    else:
                        logging.info(u'断言关键字:%s，断言成功' % assert_word)
                        self.excelObj.write_cell(sheet=user_sheet,
                                                 content='pass',
                                                 row_number=idx+2,
                                                 column_number=login_testResult,
                                                 style='green')
                        self.excelObj.write_cell_currenttime(user_sheet, row_number=idx+2, column_number=login_testTime)
                    driver.quit()
        except Exception as e:
            raise e


if __name__ == '__main__':
    Login().test_login()
    print(u'登录成功')