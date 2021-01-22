# -*- coding: utf-8 -*-
"""Python Essentials: Introduction to Python.
<Name> Lokesh
<Class> Mth 520
<Date> 1/15/21
"""

def pig_latin(word):
    if word[0] in ("a","e","i","o","u","y"): #sometimes y
        return print(word+"hay")
    else:
        return print(word[1:]+word[0]+"ay")



if __name__ == "__main__": 
    first ="you"
    second = "are"
    third = "correct"
    fourth ="!"
    pig_latin(first)
    pig_latin(second)
    pig_latin(third)
    pig_latin(fourth)
    
