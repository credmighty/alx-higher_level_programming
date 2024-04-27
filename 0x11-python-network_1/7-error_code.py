#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import requests
from sys import argv

if __name__ == '__main__':
    query_ = requests.get(argv[1])
    if query_.status_code >= 400:
        print('Error code: {}'.format(query_.status_code))
    else:
        print(query_.text)
