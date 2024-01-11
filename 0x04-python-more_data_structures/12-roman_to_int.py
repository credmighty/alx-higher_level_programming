#!/usr/bin/python3
def roman_to_int(roman_string):
    romanVal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    number = len(roman_string)
    valInt = romanVal[roman_string[number-1]]
    for i in range(number - 1, 0, -1):
        current = romanVal[roman_string[i]]
        previous = romanVal[roman_string[i-1]]

        if previous >= current:
            valInt += previous
        else:
            valInt -= previous

    return valInt
