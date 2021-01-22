# -*- coding: utf-8 -*-
"""Python Essentials: Introduction to Python.
<Name> Lokesh
<Class> Mth 520
<Date> 1/15/21
"""
def palindrome():
    n = 0
    for a in range(999,100,-1):
        for b in range(a,100,-1):
            x = a*b
            if x>n:
                s = str(a*b)
                if s == s[::-1]:
                    n = a*b
    return n


if __name__ == "__main__": 
    print(palindrome())
