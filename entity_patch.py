# fetching entities to assign category values to it 

import fuctional_replication
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



######################################################################################
#############------------vm-------------#######################
######################################################################################
vm_uuid = "46203c11-3ce7-4ec1-9318-0f06f5a4a8d4"  # vm name centos


def get_vm_config(vm_uuid):
    url = f"https://{PCIP}:9440/api/nutanix/v3/vms/{vm_uuid}"
    resp = requests.get(url, verify=False, auth=(username, password), headers=headers)
    if resp.status_code != 200:
        print('VM does not exist !!!')
    else:
        json_resp = resp.json()  
        # pretty_json = json.dumps(json_resp, indent=4) 
        # print(pretty_json)      #<------------------- formatted json 
        return json_resp

def patch_vm_config(vm_uuid, payload):
    url = f"https://{PCIP}:9440/api/nutanix/v3/vms/{vm_uuid}"
    # edit payload 
    del payload['status']
    payload['metadata']['categories_mapping'] = {category_name: [value]}
    payload['metadata']['categories'] = {category_name: value}

    # pretty_payload = json.dumps(payload, indent=4)
    # print(pretty_payload)      #<------------------- formatted json


    resp = requests.put(url, data= json.dumps(payload), verify=False, headers=headers, auth=(username, password))
    print('vm _pathing status : ', resp)


# payload = get_vm_config(vm_uuid)
# patch_vm_config(vm_uuid,payload)
# get_vm_config(vm_uuid)



######################################################################################
#############------------subnet-------------#######################
######################################################################################

subnet_uuid = 'db6495aa-ce78-468a-9156-f7be7c8aa102'  # subnet name test

def get_subnet_config(subnet_uuid):
    url = f'https://{PCIP}:9440/api/nutanix/v3/subnets/{subnet_uuid}'
    resp = requests.get(url, verify=False, headers=headers, auth=(username, password))
    # print(resp)
    if resp.status_code != 200:
        print('subnet does not exist !!!')
    else:
        json_resp = resp.json()  
        # pretty_json = json.dumps(json_resp, indent=4) 
        # print(pretty_json)      #<------------------- formatted json 
        return json_resp

def patch_subnet_config(subnet_uuid, payload):
    url = f"https://{PCIP}:9440/api/nutanix/v3/subnets/{vm_uuid}"
    # edit payload 
    del payload['status']
    payload['metadata']['categories_mapping'] = {category_name: [value]}
    payload['metadata']['categories'] = {category_name: value}

    # pretty_payload = json.dumps(payload, indent=4)
    # print(pretty_payload)      #<------------------- formatted json


    resp = requests.put(url, data= json.dumps(payload), verify=False, headers=headers, auth=(username, password))
    print('vm _pathing status : ', resp)

payload = get_subnet_config(subnet_uuid)
patch_subnet_config(subnet_uuid, payload)

