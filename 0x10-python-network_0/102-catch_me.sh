#!/bin/bash
# Send a PUT request to the specified URL 
curl -s -X PUT --header "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
