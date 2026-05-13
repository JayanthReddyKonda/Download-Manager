from manager import DownloadManager
from task import DownloadTask


def main():

    # Create manager with worker threads
    manager = DownloadManager(3)

    # Start worker pool
    manager.start_workers()

    # Create tasks
    task1 = DownloadTask("movie.mp4", 5)
    task2 = DownloadTask("song.mp3", 3)
    task3 = DownloadTask("dataset.zip", 6)
    task4 = DownloadTask("game.iso", 4)

    # Submit tasks into queue
    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)
    manager.add_task(task4)

    manager.wait_for_completion()

    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)
    manager.add_task(task4)


    # Wait until all tasks completed
    manager.wait_for_completion()

    print("\nAll downloads completed")


if __name__ == "__main__":
    main()