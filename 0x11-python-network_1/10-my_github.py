#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(user, token))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)

