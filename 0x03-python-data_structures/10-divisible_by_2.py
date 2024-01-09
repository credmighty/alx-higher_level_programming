#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2 = []
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            div_2.append(i % 2 == 0)
        return div_2
