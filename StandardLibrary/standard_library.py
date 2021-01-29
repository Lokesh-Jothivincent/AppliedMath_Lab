# standard_library.py
"""Python Essentials: The Standard Library.
<Name> Lokesh
<Class> Mth 520
<Date> 1/28/20
"""
#impoting calculator.py as cal
import calculator as cal
import itertools as ite

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    return min(L),max(L),sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    #raise NotImplementedError("Problem 2 Incomplete")
    ###check for int
    num_1 = 10
    num_2 = num_1
    num_2 = 10-1
    #print(num_1==num_2)
    print("int is immutable")
    ####check for string
    str_1 = 'abcde'
    str_2 = str_1
    str_2 = '12345'
    #print(str_2==str_1)
    print("strings are also immutable")
    ####check for list
    list_1 = [1,2,3]
    list_2 = list_1
    list_2.append(4)
    #print(list_2 == list_1)
    print("list is mutable")
    #####check for tuples
    tuple_1 = (1,2,3)
    tuple_2 = tuple_1
    #adds 1 at the end of the tuple.
    tuple_2 += (1,)
    #print(tuple_2==tuple_1)
    print("tuples are immutable")
    ####check for sets
    set_1 = {1,2,3}
    set_2 = set_1
    set_2.add(4) 
    #print(set_1==set_2)
    print("sets are mutable")

# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    temp = cal.summation(cal.multiply(a,a),cal.multiply(b,b))
    return cal.sqrt(temp)


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    temp_list = list()
    #raise NotImplementedError("Problem 4 Incomplete")
    for i in range(0,len(A)+1):
	    for element in ite.combinations(A,i):
		    temp_list.append(element)
    return temp_list


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""

#main function that calls other functions
if __name__ == "__main__":
	print(prob1([1,2,3]))
	prob2()
	print(hypot(2,2))
	print(power_set("ABC"))

