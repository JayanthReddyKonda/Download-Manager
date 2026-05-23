import threading
import time

from task import RepeatingDownload

class WorkerThread(threading.Thread):

    def __init__(self, queue, worker_name):
        super().__init__()
        self.queue = queue
        self.worker_name = worker_name
        
    def run(self):
        while True:
            task = self.queue.get()
            if task is None:
                self.queue.task_done()
                break
            print(f"[{self.worker_name}] Processing {task.filename}")
            try:
                task.execute()
            except RepeatingDownload as e:
                print(e)
            except Exception as e:
                print(f"[{self.worker_name}] Error: {e}")
                if(task.is_completed()==False):
                    if(task.retry_count>task.max_retries):
                        print(f"[{self.worker_name}] {task.filename} File Cannot Be Downloaded, Max Retries Completed")
                    else:
                        print(f"[{self.worker_name}] Process not Completed, Reinserting: {task.filename}")
                        task.retry_count += 1
                        self.queue.put(task)
            finally:
                self.queue.task_done()
        print(f"[{self.worker_name}] Stopped Gracefully")