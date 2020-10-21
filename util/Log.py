import logging
import logging.config
from VarConfig import parentDirPath


logging.config.fileConfig(parentDirPath+"\config\Logger.conf")


logger=logging.getLogger('example02')


def debug(message):

    logging.debug(message)

def warning(message):

    logging.warning(message)

def info(message):

    logging.info(message)
