#!/usr/bin/python3


def read_file(filename=""):
    """Write a function that reads a text file (UTF8) & prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as opened_file:
        for line in opened_file:
            print(line, end='')
