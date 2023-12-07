import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Vides to Spotify Podcast"
    PROJECT_VERSION: str = "1.0.0"

    USER: str = os.getenv("USER")
    PWD: str = os.getenv("PWD")


settings = Settings()
