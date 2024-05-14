#!/usr/bin/python3
"""Takes a URL, and displays value of X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
