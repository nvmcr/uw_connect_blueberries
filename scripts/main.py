from time import sleep
import requests
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
uwID = "mamishev"


worksheet = googleSheets(
    "https://docs.google.com/spreadsheets/d/1IVVHmjfvwwHswysMITsFLjgF2K4YYH4FtAmyMdUPB8A/edit", 1038549554, "./credentials.json")
columns = worksheet.column_count

for column_selector in range(3, columns):  # Skip template
    status = worksheet.cell(3, column_selector).value
    if (status is None):
        break
    if "Submitted" in status:  # ! Change to "Ready to Submit"
        print("READY TO SUBMIT!")
        print(worksheet.getColumn(column_selector))


uwConnectService = UWConnectService(username, password)

uwConnectService.getInformationFromID(uwID)

exit()


userToken = login(session, username, password)
information = getInfoFromID(session, uwID, userToken)

#
#
#
