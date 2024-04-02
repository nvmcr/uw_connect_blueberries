import os
from dotenv import load_dotenv

from GoogleSheets import googleSheets
from UWConnectService import UWConnectService

load_dotenv()  # Load .env file

username = os.getenv("UW_ID")
password = os.getenv("UW_PASSWORD")


worksheet = googleSheets(
    "https://docs.google.com/spreadsheets/d/13FJjhg-Uc_OhIxRebxAGpB-aat5aNiAwP1JWwhgmFQs/edit", 1018754358, "../credentials.json")
columns = worksheet.column_count
print(worksheet.cell(1, 1).value)
print(columns)
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
