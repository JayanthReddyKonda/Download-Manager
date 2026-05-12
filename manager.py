class DownloadManager:

    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def run_tasks(self):
        for task in self.tasks:
            if (task.is_completed()):
                print(f"Already Finished downloading {task.filename}")
                continue
            task.execute()
    