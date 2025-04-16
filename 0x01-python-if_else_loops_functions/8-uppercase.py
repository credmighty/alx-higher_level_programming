#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch = ord(i)
        if (ord(i) >= 97 and ord(i) <= 122):
            ch -= 32
        print("{}".format(chr(ch)), end='')
    print('\n', end='')
