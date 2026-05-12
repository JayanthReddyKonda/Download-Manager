from task import DownloadTask

def main():
    task1 = DownloadTask("movie.mp4", 3)
    task2 = DownloadTask("song.mp3", 1)
    task1.execute()
    task2.execute()


if __name__ == "__main__":
    main()
