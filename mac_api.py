import requests
#import pprint
from pprint import pprint

url = "https://api.macvendors.com/FC-A1-3E-2A-1C-33"

response = requests.get(url)
response.raise_for_status()

#pprint.pprint(dict(response.headers))
pprint(dict(response.headers))

print(response.status_code)
print(response.text)
print(response.cookies)
