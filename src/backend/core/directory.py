import os


class Directory:
    base_path = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )
    video_path = os.path.join(base_path, "videos")
    podcast_path = os.path.join(base_path, "podcasts")


directory = Directory()
