#!/usr/bin/python3
"""Technical interview preparation:"""


def find_peak(list_of_integers):
    """ Python function to find peak number"""
    le = len(list_of_integers)
    if le == 0:
        return
    mid = le // 2
    pivot = list_of_integers[mid]
    left = list_of_integers[mid - 1]

    if (mid == le - 1 or pivot >= list_of_integers[mid + 1]) and\
            (mid == 0 or pivot >= left):
        return pivot
    elif mid != le - 1 and list_of_integers[mid + 1] > pivot:
        return (find_peak(list_of_integers[mid + 1:]))
    return (find_peak(list_of_integers[:mid]))
