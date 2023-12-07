import os

from backend.apis.utils.spotify_upload import start_uploading
from backend.core.directory import directory
from backend.core.json_txt import read_txt, write_json


def videos():
    data = read_txt("./details.txt")

    details = {}
    for i in data:
        res = i.split("|")
        details[res[0]] = res[1]

    path = directory.video_path
    res = start_uploading(path, details)
    if res:
        write_json(f"./src/backend/core/json/videos.json", os.listdir(path))
    else:
        pass  # Log errors
