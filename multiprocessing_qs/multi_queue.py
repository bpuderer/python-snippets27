import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                #poison pill
                self.task_queue.task_done()
                break
            time.sleep(0.1)
            result = 'result from {}: {}'.format(self.name, next_task)
            self.task_queue.task_done()
            self.result_queue.put(result)

def main():
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    num_consumers = 4
    num_jobs = 20
    print 'Creating {} consumers, adding {} tasks'.format(num_consumers, num_jobs)

    consumers = [Consumer(tasks, results) for _ in xrange(num_consumers)]
    for c in consumers:
        c.start()

    for i in xrange(num_jobs):
        tasks.put('task'+str(i))

    #poison pill per consumer
    for _ in xrange(num_consumers):
        tasks.put(None)

    #wait for all of the tasks to finish
    tasks.join()

    while not results.empty():
        print results.get()

if __name__ == '__main__':
    main()
