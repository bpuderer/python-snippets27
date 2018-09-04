import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)


class MyThread(threading.Thread):

    def __init__(self, delay, repeat):
        threading.Thread.__init__(self)
        self.delay = delay
        self.repeat = repeat

    def run(self):
        """to subclass Thread, override run"""
        logger.debug('started')
        for _ in range(self.repeat):
            time.sleep(self.delay)
            logger.debug(time.ctime())
        logger.debug('completed')


def main():
    t = MyThread(1, 5)
    t.start()
    logger.debug('main completed')

if __name__ == '__main__':
    main()
