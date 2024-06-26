#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id found in the response header
    """

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
