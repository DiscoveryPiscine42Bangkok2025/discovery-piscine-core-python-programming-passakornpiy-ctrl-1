#!/usr/bin/env python3
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
result = num1 * num2
print(f"{num1} x {num2} = {result}")
if (result > 0):
    print("This number is positive.")
elif (result < 0):
    print("This number is negative.")
else:
    print("This number is both positive and negative.")