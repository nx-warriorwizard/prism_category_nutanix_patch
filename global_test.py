import fuctional_replication
import secrets
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = secrets.username
password = secrets.password
category_name = "DG_test"
value = "GroupA"
headers = {'content-type': 'application/json'}
PCIP = secrets.PCIP

def fetch_category_entity():
    url = f"https://{PCIP}:9440/api/nutanix/v3/category/query"
    payload = {
    "usage_type": "APPLIED_TO",
    "category_filter": {
    "kind_list": [
        "vm"
    ],
    "type": "CATEGORIES_MATCH_ANY",
    "params": {
        category_name: [
        value
        ]
    }}}
    
    resp = requests.post(url, verify=False, auth=(username,password), headers=headers, json=payload)
    print(resp.status_code)
    pretty_json = json.dumps(resp.json(), indent=4)
    print(pretty_json)

fetch_category_entity()
