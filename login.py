from time import sleep
import random
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver


def login(username, password):
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    # Make initial GET request to uwconnect.uw.edu, to then be redirected to UW IdP
    driver.get("https://uwconnect.uw.edu/")

    # Set username and password fields
    driver.find_element(By.ID, "weblogin_netid").send_keys(username)
    driver.find_element(By.ID, "weblogin_password").send_keys(password)

    # Sleep for 500-1500 ms so that server won't consider the request malicious.
    sleep((1000+random.randint(-500, 500))/1000)

    driver.find_element(By.ID, "submit_button").click()

    # Get JSESSIONID cookie, this is one of the two tokens we need
    jsession = driver.get_cookie("JSESSIONID")

    userToken = ""
    # Loop through each request header to find X-UserToken, which is the second token we need
    for request in driver.requests:
        header = request.headers
        userToken = header.get("X-UserToken")
        if userToken is not None:
            break

    logging.info(msg="JSESSIONID: " + jsession.get("value") +
                 " | X-UserToken: " + userToken)
