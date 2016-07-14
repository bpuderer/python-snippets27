import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def consumer(cond):
    logging.debug('started')
    #using Condition's context manager, acquire() called when block entered,
    #release() called when block exited
    #wait takes an optional timeout
    #wait releases the lock, blocks, awoken/timed out, then reacquires the lock and returns
    with cond:
        cond.wait()
        logging.debug('resource now available to consumer')

def consumer_non_cm(cond):
    logging.debug('started')
    #lock must be acquired before blocking with wait() else RuntimeError
    cond.acquire()
    cond.wait()
    logging.debug('resource now available to consumer')
    #lock must be released since it was reacquired
    cond.release()

def producer(cond):
    logging.debug('started')
    with cond:
        logging.debug('making resource available')
        #notify_all wakes up all threads
        #there's also notify(n=1) to wake up at most n threads
        cond.notify_all()


def main():
    #can optionally take a Lock or RLock. new RLock used if not provided
    #http://stackoverflow.com/questions/7424590/threading-condition-vs-threading-event
    condition = threading.Condition()

    c1 = threading.Thread(target=consumer, name='Consumer-1', args=(condition,))
    c2 = threading.Thread(target=consumer_non_cm, name='Consumer-2', args=(condition,))
    c1.start()
    c2.start()

    time.sleep(2)
    p = threading.Thread(target=producer, name='Producer-1', args=(condition,))
    p.start()

    logging.debug('main finished')

if __name__ == '__main__':
    main()
