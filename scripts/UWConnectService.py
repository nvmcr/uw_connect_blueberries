from time import sleep
import random
import requests
import xml.etree.ElementTree as ET

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from seleniumwire import webdriver


class UWConnectService:
    def __init__(self, username, password, webpage_url) -> None:
        self.session = requests.Session()
        options = Options()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)

        # Make initial GET request to uwconnect.uw.edu, to then be redirected to UW IdP
        self.driver.get(webpage_url)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'weblogin_netid')))

        # Set username and password fields
        self.driver.find_element(By.ID, "weblogin_netid").send_keys(username)
        self.driver.find_element(
            By.ID, "weblogin_password").send_keys(password)

        # Sleep for 500-1500 ms so that server won't consider the request malicious.
        sleep((1000+random.randint(-500, 500))/1000)
        self.driver.find_element(By.ID, "submit_button").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sp_formfield_fin_contact_number')))

    def nonTravel(self, data_type, data_given):
        creator = ""
        uwID = ""
        phone_number = ""
        employee_status = ""
        associated_dep = ""
        business_purp = ""
        type_money = True
        total_amount = ""
        expense_item = ""
        description_item = ""
        quantity = ""
        per_unit_cost = ""
        sales_tax = ""
        business_purp_item = ""
        multiple_sources = ""
        company = ""
        driver_worktag = ""
        driver_resource = ""
        additional_info = ""
        # Page is loaded
        for i in range(len(data_type)):
            dtype = data_type[i]
            dgiven = data_given[i]
            match dtype:
                case "Who is this request for":
                    creator = dgiven == "Someone else"  # someone else
                case "UW Net ID":
                    uwID = dgiven
                case "Contact number":
                    phone_number = dgiven
                case "Employee Status (Staff, Faculty or Student Employee)":
                    employee_status = dgiven
                case "What is your associated department or unit?":
                    associated_dep = dgiven
                case "Business Purpose and Description":
                    business_purp = dgiven
                case "Direct Deposit or Check?":
                    type_money = dgiven == "Check"
                case "Total Amount":
                    total_amount = dgiven
                case "Expense Items":
                    expense_item = dgiven
                case "Description of Item":
                    description_item = dgiven
                case "Quantity":
                    quantity = dgiven
                case "Per Unit Amount":
                    per_unit_cost = dgiven
                case "Was Sales Tax Paid?":
                    sales_tax = dgiven
                case "Business Purpose":
                    business_purp_item = dgiven
                case "Are there multiple funding sources needed? (Most likely no)":
                    multiple_sources = dgiven
                case "Company (Use UW1861 University of Washington)":
                    company = dgiven
                case "Driver Worktag Type":
                    driver_worktag = dgiven
                case "Driver Resource  Mamishev codes":
                    driver_resource = dgiven
                case "Additional info":
                    additional_info = dgiven

        self.click_element(
            '//*[@id="sp_formfield_fin_request_for"]/div/label[' + str(creator+1) + ']/span')
        self.send_element('//*[@id="sp_formfield_fin_uw_netid"]', uwID)
        self.send_element(
            '//*[@id="sp_formfield_fin_contact_number"]', phone_number)
        self.click_element(
            '//*[@id="s2id_sp_formfield_trvln_base_employee_status"]/a')
        sleep(1)
        self.click_element(
            '//div[@class="select2-result-label" and text()="'+employee_status+'"]')
        self.send_element(
            '//*[@id="sp_formfield_trvln_base_associated_dept"]', associated_dep)
        self.send_element(
            '//*[@id="sp_formfield_trvln_base_purpose"]', business_purp)
        self.click_element(
            '//*[@id="sp_formfield_trvln_base_reimb_type"]/div/div['+str(type_money+1)+']/label/span')
        self.send_element(
            '//*[@id="sp_formfield_trvln_base_exp_total"]', total_amount)
        self.click_element(
            '//*[@id="a06b6a6c1b6ae9d0cc990dc0604bcbaf_add_row"]')
        sleep(2)
        self.click_element('//*[@id="s2id_sp_formfield_trvln_exp_items"]/a')
        sleep(1)
        self.click_element(
            '//div[@class="select2-result-label" and text()="'+expense_item+'"]')
        self.send_element(
            '//*[@id="sp_formfield_trvln_exp_item_description"]', description_item)
        self.send_element(
            '//*[@id="sp_formfield_trvln_exp_line_qty"]', quantity)
        self.send_element(
            '//*[@id="sp_formfield_trvln_exp_line_per_unit"]', per_unit_cost)
        self.send_element(
            '//*[@id="sp_formfield_trvln_exp_line_total_amt"]', total_amount)
        self.click_element(
            '//*[@id="s2id_sp_formfield_trvln_exp_sales_tax_paid"]/a')
        self.click_element(
            '//div[@class="select2-result-label" and text()="'+sales_tax+'"]')
        if business_purp_item == "":
            business_purp_item = business_purp
        self.send_element(
            '//*[@id="sp_formfield_trvln_exp_bus_purpose"]', business_purp_item)
        self.click_element('//*[@id="mrvs_save_button"]')
        sleep(1)
        self.click_element('//*[@id="label_71dfba878766e9546f1997dd3fbb35b7"]')
        self.click_element(
            '//*[@id="s2id_sp_formfield_trvln__confirm_multiple_funding_sources_needed"]/a')
        self.click_element(
            '//div[@class="select2-result-label" and text()="'+multiple_sources+'"]')
        self.click_element('//*[@id="s2id_sp_formfield_fdm_budget_company"]/a')
        self.send_element('//*[@id="s2id_autogen7_search"]', company)
        sleep(2)
        self.click_element(
            '//div[@class="select2-result-label" and contains(text(), "'+company+'")]')
        self.click_element('//*[@id="s2id_sp_formfield_worktag_type"]/a')
        self.click_element(
            '//div[@class="select2-result-label" and text()="'+driver_worktag+'"]')
        sleep(1)
        self.click_element('//*[@id="s2id_sp_formfield_driver_grant"]/a')
        self.send_element('//*[@id="s2id_autogen12_search"]', driver_resource)
        sleep(2)
        self.click_element(
            '//div[@class="select2-result-label" and contains(text(), "'+driver_resource+'")]')
        self.send_element(
            '//*[@id="sp_formfield_additional_comments"]', additional_info)
        self.click_element('//*[@id="attachment_add"]')
        sleep(10)
    
    
    def click_element(self, XPATH_statement):
        self.driver.find_element(By.XPATH, XPATH_statement).click()

    def send_element(self, XPATH_statement, key):
        self.driver.find_element(By.XPATH, XPATH_statement).send_keys(key)
