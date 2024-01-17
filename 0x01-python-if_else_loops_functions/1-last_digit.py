#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ls_dg = number % 10
else:
    ls_dg = ((number * -1) % 10) * -1
if ls_dg < 6 and ls_dg != 0:
    print(f"Last digit of {number:d} is {ls_dg:d}\
 and is less than 6 and not 0")
elif ls_dg > 5:
    print(f"Last digit of {number:d} is {ls_dg:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {ls_dg:d} and is 0")

