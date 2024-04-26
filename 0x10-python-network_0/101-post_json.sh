#!/bin/bash
# Send a POST request with the JSON content to the URL
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
