# -*- coding: utf-8 -*-
"""Python Essentials: Introduction to Python.
<Name> Lokesh
<Class> Mth 520
<Date> 1/15/21
"""
def alter_list(a):
    a.append("eagle")
    print("add eagle to the end...",a)
    a[2] = "fox"
    print("fox is added at index=2...",a)
    a.remove(a[1])
    print("remove index at 1...",a)
    a.reverse()
    print("recverse the list",a)
    a[a.index("eagle")] = "hawk"
    print("replace eagle with hawk...",a)
    a.append("hunter")
    print("add hunter to the end...",a)


if __name__ == "__main__":
    my_list = ["bear","ant","cat","dog"]
    print("intial lsit...",my_list)
    alter_list(my_list)