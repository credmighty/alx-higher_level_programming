#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    query_ = response.read()

print('Body response:')
print('\t- type: {}'.format(type(query_)))
print('\t- content: {}'.format(query_))
print('\t- utf8 content: {}'.format(query_.decode('utf-8')))
