import logging
import Queue
import threading
import time
import urllib2


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
logger = logging.getLogger(__name__)

hosts = ["http://google.com", "http://apple.com", "http://youtube.com",
         "http://redhat.com", "http://ibm.com", "http://canonical.com"]

q = Queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        logger.debug('started')
        while True:
            #get host from queue
            host = self.q.get()
            logger.debug('processing %s', host)
            logger.debug(urllib2.urlopen(host, timeout=5).read(1024))
            #tell queue processing complete
            self.q.task_done()


def main():
    #create a pool of threads to process the queue
    for _ in range(3):
        t = ThreadUrl(q)
        t.daemon = True
        t.start()

    #add hosts to queue
    for host in hosts:
        q.put(host)
 
    #wait until queue processed
    q.join()
    logger.debug('threads currently alive: %s', threading.enumerate())
    logger.debug('main completed')

if __name__ == '__main__':
    main()

