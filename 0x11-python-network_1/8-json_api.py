#!/usr/bin/python3
"""Takes a letter and sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) <= 1:
        q = ""
    else:
        q = sys.argv[1]

    params = {'q': q}
    response = requests.post(url, params=params)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
