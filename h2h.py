import requests
from getpass import getpass
import sys

def h2h_intent(username, password):
    """Connect two Hosts
    """

    url = "http://localhost:8181/onos/v1/intents"
    hosts = {
            "type": "HostToHostIntent",
            "appId": "org.onosproject.ovsdb",
            "priority": 55,
            "one": "46:01:D8:96:93:A2/-1",
            "two": "BE:3B:6A:60:58:6E/-1"
            }

    response = requests.post(url, json=hosts, auth=(username, password))
    return response

def main():
    username = input("Username: ")
    password = getpass()

    print(h2h_intent(username, password))

    return 0

if __name__ == "__main__":
    sys.exit(main())
