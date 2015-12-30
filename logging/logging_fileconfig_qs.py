import logging
import logging.config
import time

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('log01')
logging.Formatter.converter = time.gmtime

logger.debug("message at debug level")
logger.info("message at info level")
logger.warning("message at warning level")
logger.error("message at error level")
logger.critical("message at critical level")
