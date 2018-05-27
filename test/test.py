#test.py
import mylog as logging
import test1
import test2


LOG = logging.getLogger(__name__)

def main():
    LOG.info("test info message:test1.TestLog1()")
    test1.TestLog1()
    # LOG.info("test info message: test1.TestLog2()")
    test2.TestLog2()


if __name__ == '__main__':
    main()