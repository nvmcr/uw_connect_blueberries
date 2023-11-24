import logging
import os
from dotenv import load_dotenv

from login import login

load_dotenv()  # Load .env file

levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG

}


# Set logging severity
logging.getLogger("seleniumwire.server").setLevel(level=levels.get("error"))
logging.getLogger("selenium").setLevel(level=levels.get("error"))

logging.getLogger("root").setLevel(level=levels.get(os.getenv("LOG_LEVEL")))


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

login(username, password)
