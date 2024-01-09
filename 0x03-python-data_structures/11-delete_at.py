#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    cpy_list = my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del cpy_list[idx]
    return cpy_list
