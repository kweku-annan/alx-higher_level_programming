#!/usr/bin/python3
"""Takes a URL, and displays value of X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    except KeyError:
        print(None)
