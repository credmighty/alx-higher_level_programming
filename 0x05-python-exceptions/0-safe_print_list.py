#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end='')
            c += 1
        except IndexError:
            pass
    print()
    return c
