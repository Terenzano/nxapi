import requests
import json
from pprint import pprint

"""
Modify these please
"""
# For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
# For basic authentication using username & pwd, set 'client_cert_auth' to False.

switchuser = 'admin'
switchpassword = 'Admin_1234!'
url = 'https://sbx-nxos-mgmt.cisco.com/ins'

myheaders = {'content-type': 'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "sid",
        "input": "show ip interface brief",
        "output_format": "json"
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))
