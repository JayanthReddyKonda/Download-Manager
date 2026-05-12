from time import sleep

class DownloadTask:
    def __init__(self,filename,duration) -> None:
        self.filename = filename
        self.duration = duration
        self.status = "pending"

    def execute(self):
        self.status = "downloading"
        print(f"Downloading {self.filename}")
        sleep(self.duration)
        self.status = "completed"
        print(f"Finished downloading {self.filename}")

    