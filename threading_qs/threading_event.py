import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')

def wait_for_event(e):
    logging.debug('event set: %s', e.is_set())
    #block until internal flag is true
    #optional timeout in seconds, method returns internal flag on exit
    e.wait()
    logging.debug('event set: %s', e.is_set())

def main():
    #internal flag initially false
    e = threading.Event()
    t = threading.Thread(target=wait_for_event, args=(e,))
    t.start()
    logging.debug('sleep before calling set()')
    time.sleep(3)
    e.set()
    logging.debug('Event is set')
    logging.debug('main completed')

if __name__ == '__main__':
    main()
