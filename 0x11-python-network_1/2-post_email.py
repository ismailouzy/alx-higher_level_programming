#!/usr/bin/python3
""" script python"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    par = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, par)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
