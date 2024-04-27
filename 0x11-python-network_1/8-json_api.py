#!/usr/bin/python3
"""Search API
"""
import requests
import sys
import json

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]

    response = requests.post(url, data={'q': q})

    try:
        data = json.loads(response.text)
        if data:
            print([f"[{user['id']}] {user['name']}" for user in data])
        else:
            print("No result")
    except json.JSONDecodeError:
        print("Not a valid JSON")
