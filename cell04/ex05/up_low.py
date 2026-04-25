#!/usr/bin/env python3
text = input()
stri = ""
for char in text:
    if (char.isupper()):
        stri = stri + char.lower()
    else:
        stri = stri + char.upper()
print(stri)