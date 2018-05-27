#test2.py
import mylog as logging

LOGGER = logging.getLogger("test2")


class TestLog2(object):
    """docstring for TestLog2"""
    def __init__(self, arg=None):
        super(TestLog2, self).__init__()
        self.arg = arg
        LOGGER.info("test2 info mesage will wirte in test2.log")
        LOGGER.warning("test2 warning mesage will wirte in test2.log")
        LOGGER.debug("test2 debug mesage will wirte in test2.log")