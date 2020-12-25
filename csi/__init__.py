import os, sys
from . import utils
from telethon.sessions import StringSession
from telethon import TelegramClient
from .dB.database import Var
from csi import csi

if Var.SESSION:
    csi = TelegramClient(StringSession(Var.SESSION), Var.API_ID, Var.API_HASH)

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio
from requests import get

ENV = os.environ.get("ENV", False)

if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)
    API_ID = int(os.environ.get("API_ID", 9))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
else:
    PLACEHOLDER = None
