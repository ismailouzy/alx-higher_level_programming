#!/usr/bin/python3
"""POST an email"""


import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)
    print(req.text)
