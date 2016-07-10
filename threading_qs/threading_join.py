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
    t1.start()
    t2.start()
    logger.debug('after starting threads. waiting for %s to complete before continuing', t2.name)
    logger.debug('is %s alive? %s', t2.name, t2.is_alive())
    #join- wait until thread terminates
    #optional float timeout arg allows continuing before thread completes
    t2.join()
    logger.debug('is %s alive? %s', t2.name, t2.is_alive())
    logger.debug('main completed')

if __name__ == '__main__':
    main()
