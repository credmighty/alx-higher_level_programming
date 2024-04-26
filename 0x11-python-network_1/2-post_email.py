#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
   request to the passed URL with the email as a parameter, and displays
   the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        query_ = response.read()

    print(query_.decode('utf-8'))
