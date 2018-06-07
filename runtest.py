import unittest
import os
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    test_dir = os.path.join(os.getcwd(), 'testScripts')
    suit = unittest.TestLoader().discover(test_dir)
    fp = open("F:\\DataDriverFrameWork\\HTMLTestRunner.html", 'wb')
    runner_test = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
    runner_test.run(suit)
    fp.close()