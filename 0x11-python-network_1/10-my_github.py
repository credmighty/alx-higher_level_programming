#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    req = requests.get(url,
                       auth=(argv[1], argv[2]))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print('None')
