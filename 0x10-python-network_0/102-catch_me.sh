#!/bin/bash
# Makes a request
curl -s -X PUT -d "user_id=98" -H "Origin: You+got+me!" -L 0.0.0.0:5000/catch_me