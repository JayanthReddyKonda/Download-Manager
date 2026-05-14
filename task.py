from time import sleep

class RepeatingDownload(Exception):
    pass


class DownloadTask:
    def __init__(self,filename,duration,max_retries=3) -> None:
        self.filename = filename
        self.duration = duration
        self.status = "pending"
        self.max_retries = max_retries
        self.retry_count = 0

    def execute(self):
        if(self.is_completed()):
            raise RepeatingDownload(f"{self.filename} Already Downloaded")
        print(f"Downloading {self.filename}")
        sleep(self.duration)
        self.status = "completed"
        print(f"Finished downloading {self.filename}")

    def is_completed(self):
        if(self.status=="completed"):
            return True
        else:
            return False
