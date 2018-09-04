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
    t1 = threading.Thread(target=some_func, args=(1, 5))
    t2 = threading.Thread(target=some_func, args=(2, 5))
    #program can exit if only daemon threads remain
    #daemon must be set before start is called
    t2.daemon = True
    t1.start()
    t2.start()
    logger.debug('main completed')

if __name__ == '__main__':
    main()
