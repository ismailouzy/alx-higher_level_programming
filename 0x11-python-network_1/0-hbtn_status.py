#!/usr/bin/python3
"""What's my status?"""

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        rap = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(rap)))
        print("\t- content: {}".format(rap))
        print("\t- utf8 content: {}".format(rap.decode('utf-8')))
