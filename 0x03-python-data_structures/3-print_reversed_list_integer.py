#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while i > 0:
        j = 0
        while j < i:
            # print("\nIs {} < {}".format(my_list[j], my_list[j + 1])) -
            # the line above display the num being tested
            if my_list[j] < my_list[j + 1]:
                # print("Switch") - this line notify switching
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            # else:
                # print("No!")
                # print("Don't Switch") - this block shows
                # when it's no swtching
            # for k in my_list:
                # print("{}".format(k), end='') - to check
                # the arrange at end of each inner loop
            j += 1
            # print()
        i -= 1
    for k in my_list:
        print("{}".format(k))
