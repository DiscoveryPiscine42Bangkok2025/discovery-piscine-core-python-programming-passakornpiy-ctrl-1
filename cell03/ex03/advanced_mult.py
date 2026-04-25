#!/usr/bin/env python3
i = 0
while (i < 11):
    stri = f"Table de {i}:"
    a = 0
    while (a < 11):
        stri = stri + " " + str(i*a)
        a += 1
    print(stri)
    i += 1