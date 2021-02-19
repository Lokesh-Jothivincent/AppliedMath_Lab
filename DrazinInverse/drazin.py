#drazin.py
"""Volume 1: The Drazin Inverse.
<Name> Lokesh
<Class> Mth 520
<Date> 2/18/21
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    if np.allclose(np.dot(A,Ad), np.dot(Ad,A)):
        if np.allclose(np.dot( np.linalg.matrix_power(A,k+1),Ad),np.linalg.matrix_power(A,k)):
            if np.allclose(np.dot(np.dot(Ad,A),Ad),Ad):
                return "True"
    return False

# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    #raise NotImplementedError("Problem 2 Incomplete")
    (row,col) = np.shape(A)
    f_more= lambda x: abs(x) >tol
    f_less = lambda x: abs(x) <= tol
    T1,Q1,k1 = la.schur (A,sort = f_more)
    T2,Q2,k2 = la.schur (A,sort = f_less)
    M = T1[:k1,:k1]
    U = Q1[:,:k1]
    U = np.column_stack((U, Q2[:,:k2]))
    '''
    print(Z1)
    print("-------------")
    print(Z2)
    print("-------------")
    '''
    U_inv = np.linalg.inv(U)
    V = np.dot(np.dot(U_inv,A),U)

    Z = np.zeros((row,col))
    row1,col1 = np.shape(V)
    #print(V[:col1,:col1])

    if col1 !=0:
        M_inv = np.linalg.inv(V[:k1,:k1])

    Z[:k1,:k1] = M_inv

    return np.dot(np.dot(U,Z),U_inv)



# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    row,col = np.shape(A)
    D=np.zeros(col)
    for each in range(col):
        D[each] = np.sum(A[:,each])
    D = np.diag(D)
    L = D-A
    L_D = drazin_inverse(L)
    row1,col1 = np.shape(L_D)
    for each in range(col1):
        L_D[each,each] = 0
    return L_D


# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")


    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")

if __name__ =="__main__":
    '''
    A= np.array([[1,3,0 ,0], [0,1,3,0], [0,0,1,3], [0,0,0,0] ])
    A_D = np.array([ [1,-3,9,81], [0,1,-3,-18], [0,0,1,3],[0,0,0,0]])
    k=1

    #print(is_drazin(A,A_D,k))
    B = np.array([ [1,1,3], [5,2,6], [-2,-1,-3] ])
    B_D = np.array([ [0,0,0,],[0,0,0],[0,0,0] ])
    kb=3
    #print(is_drazin(B,B_D,kb))

    C = np.array([ [0,0,2],[-3,2,6], [0,0,1] ])
    #print(drazin_inverse(C))
    print(is_drazin(A,drazin_inverse(A),k))
    print(is_drazin(B,drazin_inverse(B),kb))
    '''
    A = np.array([[1,0,1,1,0,0],[0,1,0,1,0,0],[1,0,1,1,0,1],[1,1,1,1,0,1],[0,0,0,0,1,1],[0,0,1,1,1,1]])
    print(effective_resistance(A))
