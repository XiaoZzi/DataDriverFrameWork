# -*- coding: utf-8 -*-
import os


# 获取DataDriverFrameWork所在目录
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath + u"\\config\\PageElementLocator.ini"

# 获取数据文件的绝对路径
dataFilePath001 = os.path.join(parentDirPath, "testData\\登录001.xlsx")
dataFilePath002 = os.path.join(parentDirPath, "testData\\联系人002.xlsx")

# 登录工作表001每列对应数字号
login_username = 2
login_password = 3
login_assert = 4
login_isExecute = 5
login_testResult = 6
login_testTime = 7

# 联系人工作表002账号工作簿中每列对应的数字序号
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 联系人工作表001add工作簿每列对应的数字序号
contracts_contractName = 2
contracts_contractMobile = 3
contracts_contractEmail = 4
contracts_assertKeyWords = 5
contracts_isExecute = 6
contracts_runTime = 7
contracts_testResult = 8