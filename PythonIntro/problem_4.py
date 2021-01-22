# -*- coding: utf-8 -*-
"""Python Essentials: Introduction to Python.
<Name> Lokesh
<Class> Mth 520
<Date> 1/15/21
"""

def first_half(a):
    """
    return first half of passed input string
    """
    length = len(a)
    # // rounds down  so middle character will be ignored if oddd number of characters are there
    return (a[:len(a)//2])

def backward(a):
    """
    return the string in reverse order using slicing [start:end:step]
    """
    return (a[-1:0:-1])


if __name__ == "__main__":
    
    str_name = "Heheeohoh"
    result1 = first_half(str_name)
    print(result1)
    result2 = backward(str_name)
    print(result2)
    

