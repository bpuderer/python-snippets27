import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

def some_func(delay, repeat):
    logger.debug('started')
    for _ in range(repeat):
        time.sleep(delay)
        logger.debug(time.ctime())
    logger.debug('completed')


def main():
    t1 = threading.Timer(5, some_func, args=(1, 5))
    t2 = threading.Timer(15, some_func, args=(2, 5))
    t1.start()
    t2.start()
    logger.debug('%s starting in 5 seconds', t1.name)
    logger.debug('%s starting in 15 seconds', t2.name)
    logger.debug('sleeping for 2 seconds before cancelling %s', t2.name)
    time.sleep(2)
    t2.cancel()
    logger.debug('%s cancelled', t2.name)
    logger.debug('main completed')

if __name__ == '__main__':
    main()
