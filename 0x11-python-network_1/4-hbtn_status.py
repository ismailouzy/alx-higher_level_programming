#!/usr/bin/python3
""" What's my status?
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    teq = req.text
    print("Body response:")
    print("\t- type: {}".format(type(teq)))
    print("\t- content: {}".format(teq))
