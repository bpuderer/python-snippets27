import logging
import logging.config
import time
import yaml

with open("logging.yaml", 'r') as f:
    parsed_yaml = yaml.load(f)

logging.config.dictConfig(parsed_yaml)
logger = logging.getLogger('log01')
logging.Formatter.converter = time.gmtime

logger.debug("message at debug level")
logger.info("message at info level")
logger.warning("message at warning level")
logger.error("message at error level")
logger.critical("message at critical level")
