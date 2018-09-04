import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

def some_func(delay, repeat, lock):
    logger.debug('started')
    lock.acquire()
    logger.debug('lock acquired')
    for _ in range(repeat):
        time.sleep(delay)
        logger.debug(time.ctime())
    lock.release()
    logger.debug('lock released')
    logger.debug('completed')

def some_func_cm(delay, repeat, lock):
    logger.debug('started')
    #using Lock's context manager, acquire() called when block entered,
    #release() called when block exited
    with lock:
        for _ in range(repeat):
            time.sleep(delay)
            logger.debug(time.ctime())
    logger.debug('completed')


def main():
    lock = threading.Lock()
    t1 = threading.Thread(target=some_func, args=(1, 5, lock))
    t2 = threading.Thread(target=some_func_cm, args=(2, 5, lock))
    t1.start()
    t2.start()
    logger.debug('main completed')

if __name__ == '__main__':
    main()
