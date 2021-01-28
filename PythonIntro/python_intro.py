# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Lokesh 
<Class> Mth 520
<Date> 1/22/21
"""
def sphere_volume(r):
	return((4/3) * 3.14159 * (r**3))

def isolate(a,b,c,d,e):
    print(a,end='     ')
    print(b,end='     ')
    print(c,d,e, sep=' ')

def first_half(a):
    """
    return first half of passed input string
    """
    # // rounds down  so middle character will be ignored if oddd number of characters are there
    return (a[:len(a)//2])

def backward(a):
    """
    return the string in reverse order using slicing [start:end:step]
    """
    return (a[-1::-1])

def list_ops():
	temp_list = ["bear", "ant", "cat", "dog"]
	temp_list.append("eagle")
	#print(temp_list)
	temp_list[2]= "fox"
	#print(temp_list)
	temp_list.remove(temp_list[1])
	#print(temp_list)
	temp_list.reverse()
	#print(temp_list)
	temp_list.append("hunter")
	return temp_list


def pig_latin(word):
	if word[0] in 'aeiou':
		word +='hay'
	else:
		word = word[1:]+word[0]+'ay'
	return word


    
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
def alt_harmonic(n):
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
#    print("Hello, world!")
#    print("Problem:2")
#    print("Volume of sphere with r= 1m is")
#    print(sphere_volume(1))
#    print("Problem:3")
#    isolate(1,2,3,4,5)
#    print("Problem:4")
#    str_name = "Heheeohoh"
#    result1 = first_half(str_name)
#    print(result1)
#    result2 = backward(str_name)
#    print(result2)
#    print("Problem:5")
#    my_list = ["bear","ant","cat","dog"]
#    print("intial lsit...",my_list)
    list_ops()
#    print("Problem:6")
#    first ="you"
#    second = "are"
#    third = "correct"
#    fourth ="!"
#    pig_latin(first)
#    pig_latin(second)
#    pig_latin(third)
#    pig_latin(fourth)
#    print("Problem:7")
#    print(palindrome())
#    print("Problem:8")
#    print(alt_harmonic(500000))
#    
    
    