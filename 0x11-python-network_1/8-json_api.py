#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
   request to the passed URL with the email as a parameter, and finally
   displays the body of the response."""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dict = req.json()
        id, name = req_dict.get('id'), req_dict.get('name')
        if len(req_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
