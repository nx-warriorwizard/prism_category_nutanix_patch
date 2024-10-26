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


def get_cat_key(category_name):
    url = f'https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}'
    resp = requests.get(url,headers=headers, auth=(username,password), verify=False)
    if resp.status_code != 200:
        print('This key does not exist ')
    return resp

def get_cat_val(category_name, value):
    url = f'https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}/{value}'
    resp = requests.get(url,headers=headers, auth=(username,password), verify=False)
    if resp.status_code != 200:
        print('This val does not exist ')
    return resp

def create_cat_key(category_name):
    payload = {
        "description": "string",
        "capabilities": {
            "cardinality": 1
        },
        "name": f'{category_name}'
        }
    url = f'https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}'
    resp = requests.put(url, verify=False, headers=headers, auth=(username,password),json= payload)
    if get_cat_key(category_name).status_code ==200:
        print('category key created succesfully !!!')
    return resp

def create_cat_val(value):
    payload = {
        "value": f'{value}'
    }
    url = f'https://{PCIP}:9440/api/nutanix/v3/categories/{category_name}/{value}'
    resp = requests.put(url, verify=False, headers=headers, auth = (username,password), json = payload)
    if get_cat_val(value).status_code ==200:
        print('category value created succesfully !!!')
    return resp



# create_cat_key(category_name)
# create_cat_val(value)



