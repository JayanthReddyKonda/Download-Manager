import threading
import time

class WorkerThread(threading.Thread):

    def __init__(self, queue, worker_name):
        super().__init__()
        self.queue = queue
        self.worker_name = worker_name
        
    def run(self):
        while True:
            task = self.queue.get()
            print(f"[{self.worker_name}] Processing {task.filename}")
            if (task.is_completed()):
                self.queue.task_done()
                print(f"Already Finished downloading {task.filename}")
                continue
            task.execute()
            self.queue.task_done()
            if(task.is_completed()==False):
                print(f"[{self.worker_name}] Process not Completed,Reinserting-{task.filename}")
                self.queue.put(task)

                
            
