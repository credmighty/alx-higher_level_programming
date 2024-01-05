#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, sub, mul
    n = sys.argv

    if len(n) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(n[1])
    b = int(n[3])

    if n[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif n[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    elif n[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif n[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
