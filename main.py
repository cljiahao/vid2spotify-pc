import argparse

from src.backend.apis.youtube import youtube
from src.backend.apis.videos import videos


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Videos to Podcast and upload to Spotify"
    )
    parser.add_argument(
        "-y",
        "-youtube",
        action="store_true",
        help="Downloads from Youtube, Convert to MP3 and upload to Spotify",
    )
    parser.add_argument(
        "-v",
        "-videos",
        action="store_true",
        help="Convert Videos to MP3 and upload to Spotify",
    )
    args = parser.parse_args()

    if args.youtube:
        youtube()
    elif args.videos:
        videos()
