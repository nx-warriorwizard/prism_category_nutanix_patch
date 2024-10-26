headers = {'content-type': 'application/json'}
username = '@@{PC_creds.username}@@'
username_secret = '@@{PC_creds.secret}@@'
category_name = "CALM_VMs"

URL1 = "https://@@{PCIP}@@:9440/api/nutanix/v3/categories/{}/{}".format(category_name,"@@{calm_project_name}@@")

method="GET"
payload = ""
resp = urlreq(URL1, verb=method, params=json.dumps(payload), headers=headers, auth='BASIC', user=username, passwd=username_secret,verify=False)
if resp.ok:
  print("Response Ok for: ",URL1)
  print("Category Found")
  json_resp = json.loads(resp.content)
  print json_resp

else:
  print(resp)
  #print(resp.content)
  print("Creating Category")
  payload = {"value":"@@{calm_project_name}@@"}
  method="PUT"
  resp2 = urlreq(URL1, verb=method, params=json.dumps(payload), headers=headers, auth='BASIC', user=username, passwd=username_secret,verify=False)
  if resp2.ok:
    print("Response Ok for: ",URL1)
    print("Category Created")
    sleep(2)
  else:
    print(resp)
    print(resp.content)
    exit(1)
    

##########################
URL2 = "https://localhost:9440/api/nutanix/v3/vms/@@{VM1.id}@@"
method="GET"
resp = urlreq(URL2, verb=method, headers=headers, auth='BASIC', user=username, passwd=username_secret,verify=False)
if resp.ok:
  print("Response Ok for: ",URL2)
  json_resp = json.loads(resp.content)
  print json_resp
else:
  print(resp)
  print(resp.content)
  sleep(2)
  
payload2 = json_resp
del payload2['status']

payload2['metadata']['use_categories_mapping'] = True
payload2['metadata']['categories_mapping'][category_name] = [ "@@{calm_project_name}@@" ]


URL3 = "https://localhost:9440/api/nutanix/v3/vms/@@{VM1.id}@@"
method="PUT"
resp = urlreq(URL2, verb=method, params=json.dumps(payload2), headers=headers, auth='BASIC', user=username, passwd=username_secret,verify=False)
if resp.ok:
  print("Response Ok for: ",URL3)
  json_resp = json.loads(resp.content)
  print json_resp
  sleep(10)
else:
  print(resp)
  print(resp.content)
  sleep(2)