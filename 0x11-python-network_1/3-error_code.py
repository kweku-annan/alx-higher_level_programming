#!/usr/bin/python3
"""Takes a URL, sends a request, and displays response"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_bytes = response.read()
            print(response_bytes.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
