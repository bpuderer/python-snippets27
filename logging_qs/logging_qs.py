import logging
import logging.handlers
import time

LOG_FILENAME = "logging_qs.log"

#create logger
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

#create handler
#logger and handlers both have setLevel methods since
#loggers can have multiple handlers
#https://docs.python.org/2/library/logging.handlers.html
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.DEBUG)

#create formatter
logging.Formatter.converter = time.gmtime
#https://docs.python.org/2/library/logging.html#logrecord-attributes
#2015-12-29T05:03:21.109Z|DEBUG|message at debug level
formatter = logging.Formatter('%(asctime)s.%(msecs)03dZ|%(levelname)s|%(message)s', '%Y-%m-%dT%H:%M:%S')

#add formatter to handler
handler.setFormatter(formatter)

#add handler to logger
logger.addHandler(handler)


logger.debug("message at debug level")
logger.info("message at info level")
logger.warning("message at warning level")
logger.error("message at error level")
logger.critical("message at critical level")
