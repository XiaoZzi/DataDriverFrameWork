#mylog.py
import logging
import logging.config
from config.VarConfig import parentDirPath


def getLogger(name='root'):
    CONF_LOG = parentDirPath + u'\\test\\logging.conf'
    # CONF_LOG = parentDirPath + u'\\util\\Logger.conf'
    logging.config.fileConfig(CONF_LOG)

    return logging.getLogger(name)


if __name__ == '__main__':
    getLogger(name='root')