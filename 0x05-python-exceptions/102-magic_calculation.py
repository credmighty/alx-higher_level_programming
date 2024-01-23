#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for c in range(1, 3):
        try:
            if c > a:
                raise Exception('Too far')
            else:
                result += a ** b / c
        except Exception:
            result = b + a
            break
    return (result)
