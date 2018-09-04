import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

def some_func(delay, repeat):
    logger.debug('%s started', threading.current_thread().name)
    for _ in range(repeat):
        time.sleep(delay)
        logger.debug(time.ctime())
    logger.debug('completed')


def main():
    #name autogen'd to Thread-n
    #args, kwargs for target invocation
    t1 = threading.Thread(target=some_func, args=(1, 5))
    t2 = threading.Thread(target=some_func, name='t2', kwargs={'delay': 2, 'repeat': 5})
    t1.start()
    t2.start()
    logger.debug('threads currently alive: %s', threading.enumerate())
    logger.debug('main completed')

if __name__ == '__main__':
    main()
