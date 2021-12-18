import requests
import json

url="https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

headers={
    "Content-type":"application/json",
    "Accept":"application/json",
    "Authorization":"Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="
}

payload=None

response=requests.post(url,headers=headers,data=payload)
if(response.status_code >= 200 and response.status_code <= 299): 
    print("GETTING TOKEN.....STATUS OK: {}".format(response.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(response.status_code,response.json()))
token=response.json()['Token']

url2="https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

headers2={
    "Content-type":"application/json",
    "Accept":"application/json",
    "x-auth-token":""
}
headers2["x-auth-token"]=token

response2=requests.request('GET',url2,headers=headers2,data=payload)

if(response.status_code >= 200 and response.status_code <= 299): 
    print("GETTING NETWORK DEVICES INFORMATION.....STATUS OK: {}".format(response.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(response.status_code,response.json()))

response2_json=response2.json()
print("DEVICE MODEL                  SERIAL NUMBER  IP ADDRESS")
for each in response2_json["response"]:
    print (each ["type"]," ",each["serialNumber"]," ",each["managementIpAddress"])


