from login import login


def getInfoFromID(session, uwID, userToken):
    informaton = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'application/xml, text/xml',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://uwconnect.uw.edu/finance?id=sc_cat_item&sys_id=9b6422601b6ae9d0cc990dc0604bcbb3',
        'Content-Type': 'application/x-www-form-urlencoded',
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

    data = {
        'sysparm_processor': 'UWNetidCheckAjax',
        'sysparm_name': 'getInformation',
        'sysparm_uwnetid': uwID,
    }

    response = session.post('https://uwconnect.uw.edu/xmlhttp.do',
                            headers=headers, data=data)
    content = str(response.content)

    start = content.find("contactNumber&quot;:&quot;") + \
        len("contactNumber&quot;:&quot;")
    end = content.find("&quot;,&quot;eid")
    phoneNumber = content[start:end]
    informaton["phone_number"] = phoneNumber
    print(phoneNumber)
    start = content.find("email&quot;:&quot;") + len("email&quot;:&quot;")
    end = content.find("&quot;,&quot;firstName")
    email = content[start:end]
    informaton["email"] = email
    print(email)

    data = {
        'sysparm_processor': 'SharedEnvRoutingUtils',
        'sysparm_name': 'getPositions',
        'sysparm_uwnetid': uwID,
    }

    response = session.post('https://uwconnect.uw.edu/xmlhttp.do',
                            headers=headers, data=data)
    # print(response.content)

    content = str(response.content)

    start = content.find(
        "&quot;positions&quot;:[&quot;") + len("&quot;positions&quot;:[&quot;")
    end = content.find("&quot;]}")
    position = content[start:end]
    print(position)
    informaton["position"] = position

    data = {
        'sysparm_processor': 'SharedEnvRoutingUtils',
        'sysparm_name': 'getCostCenter',
        'sysparm_uwnetid': uwID,
        'sysparm_position': position,
    }

    response = session.post('https://uwconnect.uw.edu/xmlhttp.do',
                            headers=headers, data=data)
    # print(response.content)
    content = str(response.content)

    start = content.find("cost_center&quot;:&quot;") + \
        len("cost_center&quot;:&quot;")
    end = content.find("&quot;,&quot;company")
    cost_center = content[start:end]
    print(cost_center)
    informaton["cost_center"] = cost_center

    data = {
        'sysparm_processor': 'SharedEnvRoutingUtils',
        'sysparm_name': 'getBalancingUnit',
        'sysparm_cost_center': cost_center,
    }

    response = session.post('https://uwconnect.uw.edu/xmlhttp.do',
                            headers=headers, data=data)

    content = str(response.content)

    start = content.find("balancing_unit&quot;:&quot;") + \
        len("balancing_unit&quot;:&quot;")
    end = content.find("&quot;,&quot;shared_environment")
    balancing_unit = content[start:end]
    print(balancing_unit)
    informaton["balancing_unit"] = balancing_unit
    start = content.find("shared_environment&quot;:&quot;") + \
        len("shared_environment&quot;:&quot;")
    end = content.find("&quot;}\"")
    shared_environment = content[start:end]
    print(shared_environment)
    informaton["shared_environment"] = shared_environment
    return informaton
