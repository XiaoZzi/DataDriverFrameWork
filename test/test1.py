#test1.py
import mylog as logging

LOGGER = logging.getLogger("test1")


class TestLog1(object):
    """docstring for TestLog1"""
    def __init__(self, arg=None):
        super(TestLog1, self).__init__()
        self.arg = arg
        LOGGER.info("test1 info mesage will wirte in test1.log")
        LOGGER.warning("test1 warning mesage will wirte in test1.log")
        LOGGER.debug("test1 debug mesage will wirte in test1.log")


if __name__ == '__main__':
    LOGGER.info("test1 info mesage will wirte in test1.log")
