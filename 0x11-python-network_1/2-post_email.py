#!/usr/bin/python3
"""Takes URL and an email, sends POST request to the url"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_data = {
        'email': email
        }
    data = urllib.parse.urlencode(email_data).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
