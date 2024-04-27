#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    etat = req.status_code
    if etat < 400:
        print(req.text)
    else:
        print("Error code: {}".format(etat))
