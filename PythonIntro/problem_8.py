# -*- coding: utf-8 -*-
"""Python Essentials: Introduction to Python.
<Name> Lokesh
<Class> Mth 520
<Date> 1/15/21
"""

def sum_alt_harmonic(n):
    #alternating harmonic terms upto n startng from 1
    """
    [x+1 if x >= 45 else x+5 for x in l]
    equivalent to.....................
    for x in l:
        if x>=45: 
            x+1
        else: 
            x+5
    """
    
    
    
    
    temp_list = [-1/i if i%2==0 else 1/i for i in range(1,n+1)]
    return sum(temp_list)

if __name__ == "__main__": 
    print(sum_alt_harmonic(500000))