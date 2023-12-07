from pytube import Playlist, YouTube
from yt_dlp import YoutubeDL

from src.backend.core.json_txt import read_json
from src.backend.core.directory import directory


def yt_extract(play_url):
    play_list = Playlist(play_url)
    old_list = read_json(f"./src/backend/core/json/{play_list.title}.json")
    new_list = [x for x in play_list if x not in set(old_list)]
    video2mp3(new_list)
    descriptions = get_descriptions(new_list)

    return play_list, descriptions


def get_descriptions(video_link):
    description = {}
    for link in video_link:
        video = YouTube(link)
        video.streams.first()
        description[video.title] = video.description

    return description


def video2mp3(playlist):
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "outtmpl": "{}/%(title)s.%(ext)s".format(directory.podcast_path),
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(playlist)
