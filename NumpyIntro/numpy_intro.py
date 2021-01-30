# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name> Lokesh
<Class>Mth 520
<Date>1/29/21
"""
import numpy as np

def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""
    #raise NotImplementedError("Problem 1 Incomplete")
    A=[[3,-1,4],[1,5,-9]]
    A=np.array(A)
    B=[[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]]
    B=np.array(B)
    return A @ B


def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
    #raise NotImplementedError("Problem 2 Incomplete")
    A= np.array([[3,1,4],[1,5,9],[-5,3,1]])
    return -1*((A@A)@A)+9*A@A-15*A


def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    A=np.ones((7,7),dtype = np.int)
    A=np.triu(A)
    print(A)
    B1 = np.ones((7,7),dtype = np.int)
    B1 = -1*B1
    B1 = np.tril(B1)
    B2_1 = np.ones((7,7),dtype = np.int)
    #B2_2 = -1*np.tril(B2_1)
    #B2_3 = 5*np.triu(B2_1,k=1)
    B = -1*np.tril(B2_1) + 5*np.triu(B2_1,k=1)
    print(B)
    return np.int64(A@B@A)


def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    #raise NotImplementedError("Problem 4 Incomplete")
    copy = np.copy(A)
    #fancy indexing
    #below, entries with -ve are given TRUE bool value
    indices = copy<0
    #indices with TRUE bool value are given 0
    copy[indices] = 0
    return copy


def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    #raise NotImplementedError("Problem 5 Incomplete")
    A = np.array([[0,2,4],[1,3,5]])
    B = np.array([[3,0,0],[3,3,0],[3,3,3]])
    C = np.diag([-2,-2,-2])
    ma,na = np.shape(A)
    mb,nb = np.shape(B)
    mat,mbt = np.shape(A.T)
    first = np.zeros((mat,na))
    row_1 = np.hstack((first,A.T,np.eye(mat)))
    row_2 = np.hstack((A,np.zeros((ma,mbt)),np.zeros((2,3))))
    row_3 = np.hstack((B,np.zeros((3,mbt)),C))
    print(np.shape(row_1))
    print(np.shape(row_2))
    print(np.shape(row_3))
    return np.vstack((row_1,row_2,row_3))


def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    #raise NotImplementedError("Problem 6 Incomplete")
    new = A.sum(axis=1)
    return A/np.vstack(new)


def prob7():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    raise NotImplementedError("Problem 7 Incomplete")

if __name__ == "__main__":
	#print(prob1())
	#print(prob2())
	#print(prob3())
        #A = np.array([-3,-1,3])
        #print(prob4(A))
	#print(prob5())
	A = np.array([[1,1,0],[0,1,0],[1,1,1]])
	print(prob6(A))

