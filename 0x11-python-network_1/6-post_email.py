#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
   request to the passed URL with the email as a parameter, and finally
   displays the body of the response."""

import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)
    query_ = req.text

    print(query_)
