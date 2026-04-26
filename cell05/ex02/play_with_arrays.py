#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
newarr = []
for index in range(len(arr)):
    if (arr[index] > 5):
        newarr.append(arr[index] + 2)
print(newarr)