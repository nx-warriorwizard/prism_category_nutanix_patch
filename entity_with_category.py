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


def fetch_entity_with_cat(entity):
    # payload = {
    # "kind": entity,
    # "filter": "category_name==DG_test;category_value==GroupA",     # <---------- uncomment if want to apply filter
    # "length": 500
    # }
    payload = {
    "kind": entity,
    "length": 500
    }
    url = f"https://{PCIP}:9440/api/nutanix/v3/{entity}s/list"
    resp = requests.post(url, verify=False, auth=(username,password),headers=headers, json=payload )
    print(resp.status_code)
    json_resp = resp.json()
    # pretty_json = json.dumps(json_resp, indent=4)
    # print(pretty_json)
    return resp

def get_cluster_entity_count(entity):
    resp = fetch_entity_with_cat(entity)
    clusters = {}
    if resp.status_code == 200:
        resp = resp.json()
        for ent in resp['entities']:
            # print(entity)
            # break
            if 'cluster_reference' in ent['status']:
                cluster_name = ent['status']['cluster_reference']['name']
                # print('*' * 50)
                # print("cluster name:", cluster_name)
                # print('*' * 50)
                
                if cluster_name not in clusters:
                    clusters[cluster_name] = 1
                else:
                    clusters[cluster_name] += 1
            else:
                print("No 'cluster_reference' found for entity:", ent['status']['name'])
            
        # print("===========================================")
        print(clusters)
        cluster_with_least_entity = sorted(clusters, key=lambda x: clusters[x])
        print(f"cluster with least {entity}s:", cluster_with_least_entity)




# fetch_entity_with_cat()
entity = 'vm'  # either vm or subnet   <------------------------

get_cluster_entity_count('vm')
get_cluster_entity_count('subnet')
