#!/usr/bin/python3
"""Lists commits of a user for a particular repo"""

import sys
import requests

if __name__ == "__main__":
    args = sys.argv[1:]
    repo = args[0]
    owner = args[1]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
               'X-GitHub-Api-Version': '2022-11-28',
               'accept': 'application/vnd.github+json'
               }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data_json = response.json()
        data_json.sort(key=lambda x: x['commit']['author']['date'],
                       reverse=True)

        if len(data_json) >= 10:
            for i in range(0, 10):
                json_item = data_json[i]
                sha = json_item['sha']
                author = json_item['commit']['author']['name']
                print(f'{sha}: {author}')
        else:
            for i in range(0, len(data_json)):
                json_item = data_json[i]
                sha = json_item['sha']
                author = json_item['commit']['author']['name']
                print(f'{sha}: {author}')
