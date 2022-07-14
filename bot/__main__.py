# Copyright (c) 2022 EDM115

import os
import logging
import time
import signal

from pyrogram import idle
from . import template
from config import Config

running = True
# https://stackoverflow.com/questions/18499497/how-to-process-sigterm-signal-gracefully
def handler_stop_signals(signum, frame):
    global running
    running = False

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s"
)

LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARN)

while running:
    if __name__ == "__main__" :
        template.start()
        starttime = time.strftime("%Y/%m/%d - %H:%M:%S")
        LOGGER.info(f"Starting bot… {starttime}")
        LOGGER.info("Bot is running now ! Join @EDM115bots")
        idle()

LOGGER.info("Received SIGTERM")
stoptime = time.strftime("%Y/%m/%d - %H:%M:%S")
LOGGER.info(f"Bot stopped at {stoptime} 😪")
