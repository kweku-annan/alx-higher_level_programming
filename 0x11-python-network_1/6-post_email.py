#!/usr/bin/python3
"""Takes a URL and an email address, sends a POST request"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        'to': email
        }
    response = requests.post(url, data=data)
    print("Your email is: {}".format(email))
