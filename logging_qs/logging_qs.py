import logging
import logging.handlers
import time

LOG_FILENAME = "logging_qs.log"

#create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create handler
#logger and handlers both have setLevel methods since
#loggers can have multiple handlers
#https://docs.python.org/2/library/logging.handlers.html
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.DEBUG)

#create formatter
#https://docs.python.org/2/library/logging.html#formatter-objects
#see formatTime
#by default time.localtime() is used
logging.Formatter.converter = time.gmtime
#https://docs.python.org/2/library/logging.html#logrecord-attributes
#2016-04-29T02:47:51.009Z - __main__ - DEBUG - message at debug level
formatter = logging.Formatter('%(asctime)s.%(msecs)03dZ - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%dT%H:%M:%S')

#add formatter to handler
handler.setFormatter(formatter)

#add handler to logger
logger.addHandler(handler)


logger.debug("message at debug level")
logger.info("message at info level")
logger.warning("message at warning level")
logger.error("message at error level")
logger.critical("message at critical level")
