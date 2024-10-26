import json
import requests
import urllib3
import secrets

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = secrets.username
password = secrets.password
category_name = "DG_test"
value = "GroupA"
headers = {'content-type': 'application/json'}
PCIP = secrets.PCIP

URL1 = f"https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}/{value}"

method = "GET"
resp = requests.get(URL1, verify=False, headers= headers, auth = (username, password))

if resp.ok:
    print("Response Ok for: ",URL1)
    print("Category Found")
    json_resp = json.loads(resp.content)
    print(json_resp)

else: # creating category if it does not exist
    print('Creating Category')

    # creating category
    URL2 = f"https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}"
    payload = {
        "capabilities": {
        "cardinality": 1
        },
        "name": f'{category_name}'
    }
    # payload = {        
    #     "capabilities": {
    #     "cardinality": 1
    #     },
    #     "name": "DG_test"}

    resp = requests.put(URL2, verify=False, headers=headers, auth=(username,password),json= payload)
    # creating value

    if resp.status_code == 200:
        print("creating values")
        payload = {"value":"grp1"}
        resp2 = requests.put(URL1, verify=False, headers= headers, auth=(username,password),params= json.dumps(payload))
        if resp2.ok:
            print("Response Ok for: ",URL1)
            print("Category Created")

        else:
            print(resp)
            print(resp.content)
            exit(1)
    
