import json
from time import sleep
import xml.etree.ElementTree as ET
import logging
import os
from dotenv import load_dotenv

from GoogleSheets import googleSheets
from UWConnectService import UWConnectService

load_dotenv()  # Load .env file

levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG

}


# # Set logging severity
logging.getLogger("seleniumwire.server").setLevel(level=levels.get("error"))
logging.getLogger("selenium").setLevel(level=levels.get("error"))

logging.getLogger("root").setLevel(level=levels.get(os.getenv("LOG_LEVEL")))

username = os.getenv("UW_ID")
password = os.getenv("UW_PASSWORD")


worksheet = googleSheets(
    "https://docs.google.com/spreadshets/d/13FJjhg-Uc_OhIxRebxAGpB-aat5aNiAwP1JWwhgmFQs/edit", 1018754358, "./credentials.json")
columns = worksheet.column_count

column = []
for column_selector in range(1, columns):  # Skip template
    status = worksheet.cell(3, column_selector).value
    if (status is None):
        print("no status found")
        break
    if "Submission Stage" in status:  # ! Change to "Submission Stage"
        print("READY TO SUBMIT!")
        submit_prompts = worksheet.getColumn(1)
        column = worksheet.getColumn(column_selector)
        break  # TODO REMOVE
    else:
        print("not found")

uwConnectService = UWConnectService(
    username, password, "https://uwconnect.uw.edu/finance?id=sc_cat_item&sys_id=9b6422601b6ae9d0cc990dc0604bcbb3", submit_prompts, column)
