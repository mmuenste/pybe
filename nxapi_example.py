import requests
from pprint import pprint

user = "admin"
password = "cisco"

url = "http://192.168.181.21/api/aaaLogin.json"
payload = {
  "aaaUser": {
    "attributes": {
      "name": f"{user}",
      "pwd": f"{password}"
}}}

# request.post(...)
# Parameter von requests-post:
# url 
# Fuer den Body data=
# speziell fuer JSON json=payload
# Um Cookies mitzusenden cookies= 

auth_response = requests.post(url, json=payload)

"""
print(auth_response.status_code,
      auth_response.text,
      auth_response.cookies,
      sep="\n\n")
"""
# Response-Objekt
# Body .text
# JSON-Body .json()

#pprint(auth_response.json())

cookie = auth_response.cookies

# Vlan erstellen
vlan_url = "http://192.168.181.21/api/mo/sys/bd.json"
vlan = 35
vlan_payload = {
"bdEntity": {
  "children": [
    {
      "l2BD": {
        "attributes": {
          "fabEncap": "vlan-",
          "pcTag": "1"
}}}]}}

vlan_response = requests.post(vlan_url, json=vlan_payload, cookies=cookie)

print(vlan_response.text)
print(vlan_response.status_code)

# Vlans auslesen
children_para = {"query-target": "children",
                "rsp-prop-include": "naming-only"}

read_vlan = requests.get(vlan_url, params=children_para, cookies=cookie)
pprint(read_vlan.json())
