# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    DATABASE_ID = int(os.environ.get("DATABASE_ID", -100))
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", None)
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    FILES_STORE_BOT_UNAME = os.environ.get("FILES_STORE_BOT_UNAME", "SuperFilesStoreBot")
    DEFAULT_BLOCKED_EXTENSIONS = "srt txt jpg jpeg png torrent html aio pdf"
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", DEFAULT_BLOCKED_EXTENSIONS).split()))
