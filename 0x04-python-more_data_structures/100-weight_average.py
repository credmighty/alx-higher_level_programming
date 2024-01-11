#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    d = 0

    for tp in my_list:
        num += tp[0] * tp[1]
        d += tp[1]

    return (num / d)
