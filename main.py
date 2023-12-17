from time import sleep
import requests
import logging
import os
from submit import submit
from dotenv import load_dotenv

from login import login
from getInformationID import getInfoFromID

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

session = requests.Session()

userToken = login(session, username, password)
information = getInfoFromID(session, uwID, userToken)

#
#
#
submit["trvln_base_purpose"] = ""
submit["se_routing_shared_environment"] = information["shared_environment"]
submit["fin_uw_netid"] = uwID
submit["se_routing_related_cc"] = information["cost_center"]
submit["trvln_base_your_email"] = information["email"]
submit["se_routing_position_str"] = information["position"]
submit["se_routing_related_bu"] = information["balancing_unit"]
submit["fin_contact_number"] = information["phone_number"]
submit["trvln_confirm_total_hide"] = "100.00"
submit["trvln_base_exp_total"] = "100.00"
