#!/usr/bin/python3
"""What's my status?"""

import urllib.request
if __name__ == "__main__":

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        print("Body response:")
        print("\t- type:", type(response.read()))
        print("\t- content:", response.read())
        print("\t- utf8 content:", response.read().decode('utf-8'))
