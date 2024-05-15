#!/usr/bin/python3
"""Takes your GitHub credentials and uses the Github API
   to display your id
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    headers = {'Authorization': 'token {}'.format(password)}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data_json = response.json()
        print(data_json.get('id'))
    else:
        print(None)
