# -*- coding = utf-8 -*-
import logging
import logging.config
from config.VarConfig import parentDirPath

# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u'\config\Logger-b.conf')
# logging.config.fileConfig(parentDirPath + u'\\test\\logging.conf')
# 选择一个日志格式
logger = logging.getLogger("example01")    # or example01
# logger = logging.getLogger("test1")    # or example01


def debug(message):
    # 定义debug级别日志打印方法
    logger.debug(message)


def info(message):
    # 定义info 级别日志打印方法
    logger.info(message)


def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)


if __name__ == '__main__':
    logging.debug(u'忽忽沪沪股犹')
    logger.info(u'123')