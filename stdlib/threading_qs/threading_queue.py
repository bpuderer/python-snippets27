import logging
import Queue
import threading
import urllib2


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

hosts = ["http://google.com", "http://apple.com"]
q = Queue.Queue()

def get_url(q, url):
    logger.debug('%s started to process %s', threading.current_thread().name, url)
    q.put(urllib2.urlopen(url).read())


def main():
    for h in hosts:
        #create thread per host
        t = threading.Thread(target=get_url, args=(q, h))
        t.daemon = True
        t.start()

    #wait until one of threads does a put
    txt = q.get()
    logger.debug(txt)
    logger.debug('threads currently alive: %s', threading.enumerate())
    logger.debug('main completed')

if __name__ == '__main__':
    main()
