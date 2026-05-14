from queue import Queue
from task import DownloadTask
from worker import WorkerThread

class DownloadManager:

    def __init__(self, num_workers=5):

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

    def stop_workers(self):
        for _ in range(len(self.workers)):
            self.queue.put(None)

    def add_task(self, task):

        self.queue.put(task)

    def wait_for_completion(self):

        self.queue.join()


    