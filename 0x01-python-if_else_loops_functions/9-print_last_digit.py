#!/usr/bin/python3
def print_last_digit(num):
    if (num < 0):
        num *= -1
    print(num % 10, end="")
    return (num % 10)
