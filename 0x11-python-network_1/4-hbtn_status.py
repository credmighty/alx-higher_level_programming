#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests"""

import requests

if __name__ == '__main__':
    query_ = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(query_)))
    print('\t- content: {}'.format(query_))
