#!/usr/bin/python3
"""Fetchs 'https://alx-intranet.hbtn.io/status' and prints status"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print(
        "Body response:\n\t- type: {}\n\t- content: {}".format(
            type(response.text), response.text))
