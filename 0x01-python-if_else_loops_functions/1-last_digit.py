#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num >= 0:
    last = num % 10
else:
    last = num % -10
if num == 0:
    print(f'Last digit of {num} is {last} and is 0')
elif num > 5:
    print(f'Last digit of {num} is {last} and is greater than 5')
else:
    print(f'Last digit of {num} is {last} and is less than 6 and not 0')
