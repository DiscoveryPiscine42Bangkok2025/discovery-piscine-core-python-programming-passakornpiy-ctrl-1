#!/usr/bin/env python3
num = input("Give me a number: ")
numf = float(num)
if (numf.is_integer()):
    print("This number is an integer.")
else:
    print("This number is a decimal.")