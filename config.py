import os
from os import environ

BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_HASH", None))
API_HASH = environ.get("API_HASH", None)
DOWNLOAD_DIR = "./downloads"
