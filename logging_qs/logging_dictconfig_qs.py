import logging
import logging.config
import time
import yaml


with open('logging.yaml') as f:
    parsed_yaml = yaml.load(f)

logging.config.dictConfig(parsed_yaml)
logger = logging.getLogger(__name__)
#https://docs.python.org/2/library/logging.html#formatter-objects
#see formatTime
#by default time.localtime() is used
logging.Formatter.converter = time.gmtime

logger.debug("message at debug level")
logger.info("message at info level")
logger.warning("message at warning level")
logger.error("message at error level")
logger.critical("message at critical level")
