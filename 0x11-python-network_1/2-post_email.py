#!/usr/bin/python3
"""Takes URL and an email, sends POST request to the url"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    email_data = {
        'to': email,
        'subject': 'Hello!',
        'body': 'Test email'
        }
    data = urllib.parse.urlencode(email_data)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data=data) as response:
        print("Your email is: {}".format(data['to']))
