import requests
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = "{\n  \"aaaUser\": {\n    \"attributes\": {\n      \"name\": \"admin\",\n      \"pwd\": \"Admin_1234!\"\n    }\n  }\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "764193c2-18c4-44a3-87d3-d6030f2c6bb5,c797dd03-44fe-48d3-a898-99f5a6bc6e44",
    'Host': "sbx-nxos-mgmt.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "98",
    'Cookie': "nxapi_auth=dzqnf:0WIHwaUuPnTsrwpFl5sAdj+mAxs=; APIC-cookie=vm6WLuNnlTwvTiENOjsSn6F5/S27yeQk9Xrmzr2hRUAWxn0qqT3jW0j073uzlsksWg7BmEAtL4CRiULG1GxoALLaGaPhksQMhjoQ3zw8AwiwCtEhN2Gx1EZ1VZfrVM9d97IJSdAolHiYp7Gduo3BsyEw5Iuvdr7/QPZqqqff+oo=",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.post(
    url, data=payload, headers=headers, verify=False).json()

# pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']

pprint("This is your token: ")
pprint('*' * 50)
pprint(token)

cookies = {}
cookies['APIC-cookie'] = token


url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/1].json"

payload = "{\n    \"l1PhysIf\": {\n        \"attributes\": {\n            \"descr\": \"Configured with PYTHON DEMO\"\n        }\n    }\n}"
headers = {
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1d22ac06-f32f-4de2-818a-abc2df4d7eb7,7c4f8e71-17d8-4fb0-8e49-d4caa598a126",
    'Host': "sbx-nxos-mgmt.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "112",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

put_response = requests.put(
    url, data=payload, headers=headers, cookies=cookies, verify=False).json()


pprint(put_response)
