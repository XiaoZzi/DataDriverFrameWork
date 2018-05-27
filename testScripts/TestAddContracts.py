# -*- coding = utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from appModules.AddContractPersonAction import AddContractPerson
import traceback
from time import sleep
from util.Log import *

# 创建解析excel对象
excelObj = ParseExcel()
# 将excel数据加载到内存
excelObj.load_workbook(dataFilePath)


def launch_broswer():
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options实例中添加禁用扩展插件的设置参数项
    chrome_options.add_argument("--disable-extensions")
    # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # 添加浏览器最大化的设置参数项，一启动就最大化
    chrome_options.add_argument('--start-maximized')
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # 访问51kaihui首页
    driver.get('https://www.51kaihui.com/login/index')
    sleep(3)
    return driver


def test_add_contract():
    logging.info(u'添加联系人数据驱动测试开始')
    try:
        # 根据excel文件中sheet名称获取此sheet的对象
        user_sheet = excelObj.get_sheetbyname(u'账号')
        # 获取账号是否执行
        is_execute_user = excelObj.get_column(user_sheet, account_isExecute)
        # 获取账号sheet中的数据表列
        data_book_column = excelObj.get_column(user_sheet, account_dataBook)
        for idx, i in enumerate(is_execute_user[1:]):
            # 循环遍历账号表中的账号，为需要执行的账号添加联系人
            if i == 'y':   # 表示要执行
                # 获取第i行的数据
                user_row = excelObj.get_row(user_sheet, idx + 2)
                # print(type(user_row))
                # print(user_row[1])
                # 获取第i行用户名
                username = user_row[account_username - 1]
                # 获取第i行密码
                password = str(user_row[account_password - 1])

                # 创建浏览器实例对象
                driver = launch_broswer()
                logging.debug(u'启动浏览器，访问主页')

                # 登录邮箱
                LoginAction.login(d=driver, username=username, password=password)
                logging.debug(u'用户%s密码%s正在进行登录' %(username, password))
                sleep(3)
                try:
                    assert u'通讯录' in driver.page_source
                    logging.info(u'用户%s登录成功' % username)
                except AssertionError as e:
                    logging.info(u'用户%s登录失败, 异常信息：%s'
                                 % (username, str(traceback.format_exc())))

                # 获取第i行用户要添加的联系人数据表sheet名
                data_book_name = data_book_column[idx+1]
                # 获取对应的数据表对象
                data_sheet = excelObj.get_sheetbyname(data_book_name)
                # 获取联系人数据表中联系人是否执行
                is_execute_data = excelObj.get_column(data_sheet, contracts_isExecute)

                contract_num = 0   # 记录添加成功联系人个数
                is_execute_num = 0  # 记录需要执行联系人个数

                for id, data in enumerate(is_execute_data[1:]):
                    # 获取第id+2行对象
                    row_content = excelObj.get_row(data_sheet, id + 2)
                    # 获取联系人姓名
                    contract_person_name = row_content[contracts_contractName - 1]
                    # 获取联系人电话
                    contracts_person_mobile = row_content[contracts_contractMobile - 1]
                    # 获取联系人备注
                    contracts_person_email = row_content[contracts_contractEmail - 1]
                    # 添加联系人后断言的关键字
                    assert_keywords = row_content[contracts_assertKeyWords - 1]

                    # 寻黄遍历是否执行添加联系人列，如果被设置为添加，则进行添加
                    if data == 'y':
                        logging.debug(u'用户 %s 需要添加联系人对象 %s' % (username, contract_person_name))
                        # 如果第id行被设置为执行，则is_execute_num自增1
                        is_execute_num += 1

                        # 执行添加联系人操作
                        AddContractPerson.add(
                            d=driver,
                            contract_name=contract_person_name,
                            contract_mobile=contracts_person_mobile,
                            contract_memo=contracts_person_email)
                        sleep(1)
                        logging.debug(u'用户 %s 添加联系人对象名字%s电话%s邮箱%s' % (username,
                                                                      contract_person_name,
                                                                      contracts_person_mobile,
                                                                      contracts_person_email))

                        # 在联系人工作表写入添加联系人执行时间
                        excelObj.write_cell_currenttime(data_sheet,
                                                        row_number=id+2,
                                                        column_number=contracts_runTime)
                        try:
                            # 断言给定的关键字是否出现在页面中
                            assert assert_keywords in driver.page_source
                        except AssertionError as e:
                            # 断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelObj.write_cell(data_sheet, 'failed',
                                                row_number=id+2,
                                                column_number=contracts_testResult,
                                                style='red')
                            logging.info(u'用户 %s 添加联系人%s失败' % (username, contract_person_name), e)
                        else:
                            # 断言成功，写入添加联系人信息成功
                            excelObj.write_cell(data_sheet, 'pass',
                                                row_number=id+2,
                                                column_number=contracts_testResult,
                                                style='green')
                            contract_num += 1
                            logging.debug(u'用户 %s 添加联系人%s成功' % (username, contract_person_name))
                    else:
                        logging.debug(u'用户 %s 不需要添加联系人对象 %s' % (username, contract_person_name))

                    logging.debug('需要添加的联系人个数contractNum为 = %s, 添加成功的联系人个数isExecuteNum为 = %s'
                                  % (contract_num, is_execute_num))

                    if contract_num == is_execute_num:
                        # 如果成功添加联系人个数等于需要添加的联系人个数，说明给第i个用户添加联系人的用力执行成功
                        # 在账号工作表写入成功信息，否则写入失败信息
                        excelObj.write_cell(user_sheet, 'pass',
                                            row_number=idx + 2,
                                            column_number=account_testResult,
                                            style='green')
                        logging.debug(u'为用户%s 添加 %d个联系人，测试通过' % (username, contract_num))
                    else:
                        excelObj.write_cell(user_sheet, 'failed',
                                            row_number=idx + 2,
                                            column_number=account_testResult,
                                            style='red')
                        logging.info(u'为用户%s 添加 %d个联系人，测试失败' % (username, contract_num))
                driver.quit()

                logging.info(u'为用户%s 添加 %d个联系人，测试通过' % (username, contract_num))

            else:
                logging.info(u'用户%s被设置为忽略执行' % excelObj.get_cell_value(user_sheet,
                                                                       row_number=idx+2,
                                                                       column_number=account_username))
    except Exception as e:
        logging.info(u'数据驱动框架主程序发生异常，异常信息为：', e)
        logging.info(traceback.print_exc())


if __name__ == '__main__':
    test_add_contract()
