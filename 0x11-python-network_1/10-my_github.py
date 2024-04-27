#!/usr/bin/python3
"""access github
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

username = sys.argv[1]
token = sys.argv[2]

if __name__ == "__main__":
    auth = HTTPBasicAuth(username, token)
    resp = requests.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
