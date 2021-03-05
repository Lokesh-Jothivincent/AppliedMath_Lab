# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name> Lokesh
<Class> Mth 520
<Date> 3/3/21
"""
import numpy as np
import cvxpy as cp
from scipy.optimize import nnls 

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    x= cp.Variable(3,nonneg = True)
    c =np.array([2,1,3])
    objective  = cp.Minimize(c.T @ x)
    
    A = np.array([1,2,0])
    G = np.array([0,1,-4])
    H = np.array([2,10,3])
    P = np.eye(3)
    constraints = [A@x <=3, G@x <=1, H@x >=12,P@x >=0]
    problem = cp.Problem(objective, constraints)
    solution = problem.solve()
    
    return x.value, solution
    


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #raise NotImplementedError("Problem 2 Incomplete")
    x_var= cp.Variable(np.shape(A)[1],nonneg = True)
    c= np.array([1,1,1,1])
    objective  = cp.Minimize(cp.norm(c.T @ x_var,1))
    P = np.eye(np.shape(A)[1])
    constraints =list()
    for row in range(np.shape(A)[0]):
        constraints.append(A[row,:]@x_var==b[row,:])
    constraints.append(P@x_var>=0)
    
    problem = cp.Problem(objective, constraints)
    solution = problem.solve()

    return x_var.value,solution

# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    x= cp.Variable(6,nonneg = True)
    c =np.array([4,7,6,8,8,9])
    objective  = cp.Minimize(c.T @ x)
    
    A = np.array([1,1,0,0,0,0])
    G = np.array([0,0,1,1,0,0])
    H = np.array([0,0,0,0,1,1])
    I =np.array([1,0,1,0,1,0])
    J = np.array([0,1,0,1,0,1])
    P = np.eye(6)
    constraints = [A@x ==7, G@x ==2, H@x ==4,I@x ==5,J@x ==8,P@x >=0]
    problem = cp.Problem(objective, constraints)
    solution = problem.solve()
    
    return x.value, solution

# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #raise NotImplementedError("Problem 4 Incomplete")
    Q = np.array([[3,2,1],[2,4,2],[1,2,3]])
    r = np.array([3,0,1])
    x = cp.Variable(3)
    prob = cp.Problem(cp.Minimize(.5 * cp.quad_form(x, Q) + r.T @ x))
    sol = prob.solve()
    return x.value,sol


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #raise NotImplementedError("Problem 5 Incomplete")
    x= cp.Variable(4,nonneg =True)
    cost = np.linalg.lstsq(A, b, rcond=None)[0]
    objective = cp.Minimize(cp.norm(cost,2))
    
    #constraint part
    P=np.eye(4)
    G = np.array([1,1,1,1])
    print(np.sum(G@x) ==1)
    constraints = [P@x>=0,np.sum(G@x) ==1]
    
    prob = cp.Problem(objective,constraints)
    sol = prob.solve()
    
    return x.value,sol#1#np.array([0,1,0,0]) , 5.099


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")
    
if __name__ == "__main__":
    #print('booyeah')
    #print(prob1())
    A = np.array([[1,2,1,1],[0,3,-2,-1]])
    b = np.array([[7],[4]])
    #print(l1Min(A, b))
    #print(prob3())
    #print(prob4())
    print(prob5(A,b))