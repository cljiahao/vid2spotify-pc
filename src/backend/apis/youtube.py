from backend.apis.utils.spotify_upload import start_uploading
from backend.apis.utils.yf_download import yt_extract
from backend.core.directory import directory
from backend.core.json_txt import read_txt, write_json


def youtube():
    playlist = read_txt("./youtube_url.txt")
    play_list, descriptions = yt_extract(playlist)
    path = directory.podcast_path
    res = start_uploading(path, descriptions)
    if res:
        write_json(f"./src/backend/core/json/{play_list.title}.json", play_list)
    else:
        pass  # Log errors
