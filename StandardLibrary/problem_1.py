# -*- coding: utf-8 -*-
"""Python Essentials: The Standard Library.
<Name> Lokesh
<Class> Mth 520
<Date> 1/22/21
"""

def list_out(L):
    return (min(L),max(L),sum(L)/len(L))

if __name__ == "__main__":
    print(list_out([1,2,3,4,5]))