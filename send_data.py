import requests

item_data = {
        "purch_machinery_equip": "No",
        "optional_worktags": "",
        "driver_grant": "",
        "toggle_cost_center": "",
        "purch_total_amount_hide": "500.00",
        "purch_multiple_funding_srcs": "No",
        "purch_receiver_contact": "Caitlin DeShazo-Couchot",
        "driver_container_start": "",
        "IO:780312dbc34b3150926e19a4e40131b6": "true",
        "se_routing_shared_environment": "College of Engineering Shared Environment",
        "purch_calculate_total_confirm": "true",
        "fin_uw_netid": "mamishev",
        "purch_employee_status": "student",
        "se_routing_uwm": "false",
        "se_routing_related_cc": "CC103212",
        "purch_total_amount": "500.00",
        "toggle_default_cost_center": "",
        "se_routing_position_str": "PN-0000620 PROFESSOR, Electrical Engineering - Mamishev, Alexander V",
        "purch_ship_to_address3": "",
        "purch_assoc_dept": "Electrical and Computer Engineering",
        "purch_ship_to_address2": "",
        "purch_ship_to_address1": "2610 164TH ST SW A406",
        "purch_qualify": "",
        "se_routing_se_override_list": "",
        "optional_assignee": "",
        "fdm_budget_company": "b7722c2687f7e994b302ca64dabb3549",
        "more_information": "true",
        "se_routing_related_bu": "BU132 College of Engineering",
        "purch_ship_to_state": "Washington",
        "driver_program": "",
        "fin_purch_line_items_mrvs": "[]",
        "purch_provide_detail": "",
        "fdm_budget": "true",
        "optional_adhoc_program": "",
        "purch_home_address": "Yes",
        "se_routing_positions_list": "",
        "purch_ship_to_country": "USA",
        "fin_purchase_request_summary": "true",
        "driver_gift": "",
        "fin_request_for": "someone_else",
        "IO:f40312dbc34b3150926e19a4e40131ab": "false",
        "billing_info": "",
        "toggle_resource": "",
        "optional_container_start2": "",
        "worktag_type": "",
        "optional_container_start4": "",
        "fin_purchase_request_base": "true",
        "driver_project": "",
        "optional_container_start3": "",
        "optional_activity": "",
        "purch_email": "mamishev@uw.edu",
        "purch_ship_to_zip": "98087",
        "driver_resource": "",
        "fin_shared_requester_info": "true",
        "more_information_label": "",
        "purch_ship_to_city": "Lynnwood",
        "driver_cost_center": "",
        "overwrite_worktags": "",
        "fin_requester_info_label": "",
        "purch_approver": "mamishev",
        "toggle_container_start2": "",
        "optional_container_start": "",
        "purch_ship_to_address": "",
        "additional_comments": "If needed, use discretionary budget GF120957",
        "fin_contact_number": "+1 206 221-5729",
        "purch_uw_purpose": "Student Research Award",
        "toggle_container_start": "",
        "fin_shared_shared_environment_routing": "true",
        "optional_other_worktags": "",
        "purch_detail_label": "",
        "optional_adhoc_standalone_grant": "",
        "purch_purchase_info_label": "",
        "toggle_default_resource": "",
        "driver_activity": "",
    },

json_data = {
    "variables": item_data,
    "sysparm_item_guid": "f80312dbc34b3150926e19a4e40131aa",
    "get_portal_messages": "true",
    "sysparm_no_validation": "true",
}
item_data[""]

def sendData(session, userToken, purch_machinery_equip,optional_worktags,driver_grant,toggle_cost_center,purch_total_amount_hide,purch_multiple_funding_srcs,purch_receiver_contact,driver_container_start,se_routing_shared_environment,purch_calculate_total_confirm,fin_uw_netid,purch_employee_status,se_routing_uwm,se_routing_related_cc,purch_total_amount,toggle_default_cost_center,se_routing_position_str,purch_ship_to_address3,purch_assoc_dept,purch_ship_to_address2,purch_ship_to_address1,purch_qualify,se_routing_se_override_list,optional_assignee,fdm_budget_company,more_information,se_routing_related_bu,purch_ship_to_state,driver_program,fin_purch_line_items_mrvs,purch_provide_detail,fdm_budget,optional_adhoc_program,purch_home_address,se_routing_positions_list,purch_ship_to_country,fin_purchase_request_summary,driver_gift,fin_request_for,billing_info,toggle_resource,optional_container_start2,worktag_type,optional_container_start4,fin_purchase_request_base,driver_project,optional_container_start3,optional_activity,purch_email,purch_ship_to_zip,driver_resource,fin_shared_requester_info,more_information_label,purch_ship_to_city,driver_cost_center,overwrite_worktags,fin_requester_info_label,purch_approver,toggle_container_start2,optional_container_start,purch_ship_to_address,additional_comments,fin_contact_number,purch_uw_purpose,toggle_container_start,fin_shared_shared_environment_routing,optional_other_worktags,purch_detail_label,optional_adhoc_standalone_grant,purch_purchase_info_label,toggle_default_resource,driver_activity):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'application/xml, text/xml',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://uwconnect.uw.edu/finance?id=sc_cat_item&sys_id=ddb295871b7a6550cc990dc0604bcb69',        'Content-Type': 'application/x-www-form-urlencoded',
        'X-UserToken': userToken,
        'X-Transaction-Source': 'Interface=Web,Interface-Name=FINANCE,Interface-Type=Service Portal,Interface-SysID=800e46e3dba5bc506ccf6a9ed3961989',
        'X-Use-Polaris': 'false',
        'Origin': 'https://uwconnect.uw.edu',
        'DNT': '1',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    item_data["purch_machinery_equip"] = purch_machinery_equip
    item_data["optional_worktags"] = optional_worktags
    item_data["driver_grant"] = driver_grant
    item_data["toggle_cost_center"] = toggle_cost_center
    item_data["purch_total_amount_hide"] = purch_total_amount_hide
    item_data["purch_multiple_funding_srcs"] = purch_multiple_funding_srcs
    item_data["purch_receiver_contact"] = purch_receiver_contact
    item_data["driver_container_start"] = driver_container_start
    item_data["se_routing_shared_environment"] = se_routing_shared_environment
    item_data["purch_calculate_total_confirm"] = purch_calculate_total_confirm
    item_data["fin_uw_netid"] = fin_uw_netid
    item_data["purch_employee_status"] = purch_employee_status
    item_data["se_routing_uwm"] = se_routing_uwm
    item_data["se_routing_related_cc"] = se_routing_related_cc
    item_data["purch_total_amount"] = purch_total_amount
    item_data["toggle_default_cost_center"] = toggle_default_cost_center
    item_data["se_routing_position_str"] = se_routing_position_str
    item_data["purch_ship_to_address3"] = purch_ship_to_address3
    item_data["purch_assoc_dept"] = purch_assoc_dept
    item_data["purch_ship_to_address2"] = purch_ship_to_address2
    item_data["purch_ship_to_address1"] = purch_ship_to_address1
    item_data["purch_qualify"] = purch_qualify
    item_data["se_routing_se_override_list"] = se_routing_se_override_list
    item_data["optional_assignee"] = optional_assignee
    item_data["fdm_budget_company"] = fdm_budget_company
    item_data["more_information"] = more_information
    item_data["se_routing_related_bu"] = se_routing_related_bu
    item_data["purch_ship_to_state"] = purch_ship_to_state
    item_data["driver_program"] = driver_program
    item_data["fin_purch_line_items_mrvs"] = fin_purch_line_items_mrvs
    item_data["purch_provide_detail"] = purch_provide_detail
    item_data["fdm_budget"] = fdm_budget
    item_data["optional_adhoc_program"] = optional_adhoc_program
    item_data["purch_home_address"] = purch_home_address
    item_data["se_routing_positions_list"] = se_routing_positions_list
    item_data["purch_ship_to_country"] = purch_ship_to_country
    item_data["fin_purchase_request_summary"] = fin_purchase_request_summary
    item_data["driver_gift"] = driver_gift
    item_data["fin_request_for"] = fin_request_for
    item_data["billing_info"] = billing_info
    item_data["toggle_resource"] = toggle_resource
    item_data["optional_container_start2"] = optional_container_start2
    item_data["worktag_type"] = worktag_type
    item_data["optional_container_start4"] = optional_container_start4
    item_data["fin_purchase_request_base"] = fin_purchase_request_base
    item_data["driver_project"] = driver_project
    item_data["optional_container_start3"] = optional_container_start3
    item_data["optional_activity"] = optional_activity
    item_data["purch_email"] = purch_email
    item_data["purch_ship_to_zip"] = purch_ship_to_zip
    item_data["driver_resource"] = driver_resource
    item_data["fin_shared_requester_info"] = fin_shared_requester_info
    item_data["more_information_label"] = more_information_label
    item_data["purch_ship_to_city"] = purch_ship_to_city
    item_data["driver_cost_center"] = driver_cost_center
    item_data["overwrite_worktags"] = overwrite_worktags
    item_data["fin_requester_info_label"] = fin_requester_info_label
    item_data["purch_approver"] = purch_approver
    item_data["toggle_container_start2"] = toggle_container_start2
    item_data["optional_container_start"] = optional_container_start
    item_data["purch_ship_to_address"] = purch_ship_to_address
    item_data["additional_comments"] = additional_comments
    item_data["fin_contact_number"] = fin_contact_number
    item_data["purch_uw_purpose"] = purch_uw_purpose
    item_data["toggle_container_start"] = toggle_container_start
    item_data["fin_shared_shared_environment_routing"] = fin_shared_shared_environment_routing
    item_data["optional_other_worktags"] = optional_other_worktags
    item_data["purch_detail_label"] = purch_detail_label
    item_data["optional_adhoc_standalone_grant"] = optional_adhoc_standalone_grant
    item_data["purch_purchase_info_label"] = purch_purchase_info_label
    item_data["toggle_default_resource"] = toggle_default_resource
    item_data["driver_activity"] = driver_activity
    session.post()
    
