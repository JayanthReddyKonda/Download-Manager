from queue import Queue
from worker import WorkerThread

class DownloadManager:

    def __init__(self, num_workers):

        # Shared task queue
        self.queue = Queue()

        # Store worker objects
        self.workers = []

        # Create worker pool
        for i in range(num_workers):
            worker = WorkerThread(self.queue,f"Worker-{i+1}")
            # Daemon threads terminate automatically when main program exits
            worker.daemon = True
            self.workers.append(worker)

    def start_workers(self):

        for worker in self.workers:
            worker.start()

    def add_task(self, task):

        self.queue.put(task)

    def wait_for_completion(self):

        self.queue.join()


    