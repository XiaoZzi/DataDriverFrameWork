import logging
import sys
# exc_info:值为布尔值，当该参数值设置为True，则会将异常信息添加到日志消息中，没有异常信息则添加None
# stack_info：值为布尔值，默认为False，当设置为True时，栈信息将会被添加到日志信息中
# extra:这是一个字典（dict）参数，可以用来自定义消息格式中包含的字段，但key不能与logging模块中的字段冲突

# LOG_FORMAT = "%(asctime)s - %(levelname)s-%(user)s[%(ip)s]-%(message)s"
# DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
# logging.basicConfig(level=logging.DEBUG, filename='mylog.log', format=LOG_FORMAT,datefmt=DATE_FORMAT)
# logging.warning("someone delete the log file",
#                 exc_info=True, stack_info=True, extra={'user':'Tom','ip':'56.578.23.13'})

# 日志器需要通过处理器（handle）将日志信息输出到目标位置，如：网络，文件，sys.out等
# 日志器（logger）可以设置多个处理器，将同一条日志记录输出到不同位置
# 每个handle都可以设置自己的过滤器，以及格式器
# 简单来说，日志器logger是入口，干活的是处理器

# 使用python代码实现日志配置
# 创建一个日志器logger并设置其日志级别为DEUBUG
# logging.getLogger()方法有一个可选参数，该参数表示将要返回的日志器的名称，如果不提供，则其值为‘root’
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# 创建2个流处理器handle,并设置其级别为DEBUG
handler01 = logging.StreamHandler(sys.stdout)
handler01.setLevel(logging.DEBUG)
handler02 = logging.FileHandler('mylog.log')
handler02.setLevel(logging.ERROR)

# 为日志器创建格式器并添加到handle
formatter01 = logging.Formatter('%(asctime)s - %(name)s-%(levelname)s-%(message)s')
formatter02 = logging.Formatter('%(asctime)s / %(name)s / %(levelname)s / %(message)s')
handler01.setFormatter(formatter01)
handler02.setFormatter(formatter02)

# 为日志器logger添加上面的处理器handle
logger.addHandler(handler01)
logger.addHandler(handler02)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')



