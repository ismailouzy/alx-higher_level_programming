#!/bin/bash
# sends a request an URL
curl -s "$1" | wc -c
