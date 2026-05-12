from task import DownloadTask
from manager import DownloadManager

def main():
    task1 = DownloadTask("movie.mp4", 3)
    task2 = DownloadTask("song.mp3", 1)

    manager = DownloadManager()

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task1)
    manager.run_tasks()


if __name__ == "__main__":
    main()
