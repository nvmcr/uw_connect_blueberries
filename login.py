from time import sleep
import random
# import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver


def login(session, username, password):
    options = Options()
    # options.add_experimental_option("detach", True)
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    # Make initial GET request to uwconnect.uw.edu, to then be redirected to UW IdP
    driver.get(
        "https://uwconnect.uw.edu/finance?id=sc_cat_item&sys_id=9b6422601b6ae9d0cc990dc0604bcbb3")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'weblogin_netid')))

    # Set username and password fields
    driver.find_element(By.ID, "weblogin_netid").send_keys(username)
    driver.find_element(By.ID, "weblogin_password").send_keys(password)

    # Sleep for 500-1500 ms so that server won't consider the request malicious.
    sleep((1000+random.randint(-500, 500))/1000)
    driver.find_element(By.ID, "submit_button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sp_formfield_fin_contact_number')))

    # Get JSESSIONID cookie, this is one of the two tokens we need
    jsession = driver.get_cookie("JSESSIONID")
    selenium_cookies = driver.get_cookies()
    cookies = {}
    for cookie in selenium_cookies:
        session.cookies.set(cookie["name"], cookie["value"])

    userToken = ""
    driver.requests
    # Loop through each request header to find X-UserToken, which is the second token we need
    first = True
    for request in driver.requests:
        header = request.headers
        # print(header)
        userToken = header.get("X-UserToken")
        if userToken is not None:
            if first:
                oldToken = driver.requests[0].headers.get("X-UserToken")
            elif userToken != oldToken:
                break

    print("Active usertoken is: " + userToken)
    # logging.info(msg="JSESSIONID: " + jsession.get("value") +
    #              " | X-UserToken: " + userToken)
    return userToken
