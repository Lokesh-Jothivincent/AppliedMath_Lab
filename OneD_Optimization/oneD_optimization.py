# oneD_optimization.py
"""Volume 2: One-Dimensional Optimization.
<Name> Lokesh
<Class> Mth 520
<Date> 3/5/21
"""

import numpy as np
from scipy import optimize as opt
from matplotlib import pyplot as plt
from scipy.optimize import linesearch
from autograd import numpy as anp
from autograd import grad

# Problem 1
def golden_section(f, a, b, tol=1e-5, maxiter=15):
    """Use the golden section search to minimize the unimodal function f.

    Parameters:
        f (function): A unimodal, scalar-valued function on [a,b].
        a (float): Left bound of the domain.
        b (float): Right bound of the domain.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float): The approximate minimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    x0 = 0.5 *(a+b)
    phi = 0.5*(1+(5**0.5))
    for i in range(maxiter):
        c = (b-a)/ phi
        a_bar = b-c
        b_bar = a+c
        if f(a_bar) <= f(b_bar):
            b = b_bar
        else:
            a =a_bar
        x1 =0.5 *(a+b)
        if abs(x0-x1) <tol:
            break
        x0 = x1
        
    if i >= maxiter:
        convg = False
    else:
        convg = True
    return x1,convg,i

# Problem 2
def newton1d(df, d2f, x0, tol=1e-5, maxiter=15):
    """Use Newton's method to minimize a function f:R->R.

    Parameters:
        df (function): The first derivative of f.
        d2f (function): The second derivative of f.
        x0 (float): An initial guess for the minimizer of f.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float): The approximate minimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    x_old = x0
    for i in range(maxiter):
        x_new = x_old - df(x_old)/d2f(x_old)
        if abs(x_new - x_old) <=tol:
            break
        x_old = x_new
    if i >= maxiter:
        convg = False
    else:
        convg = True
    return x_new,convg,i
        
    


# Problem 3
def secant1d(df, x0, x1, tol=1e-5, maxiter=500):
    """Use the secant method to minimize a function f:R->R.

    Parameters:
        df (function): The first derivative of f.
        x0 (float): An initial guess for the minimizer of f.
        x1 (float): Another guess for the minimizer of f.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float): The approximate minimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    x_k1 = x0
    x_k = x1
    for i in range(maxiter):
        x_new = (x_k1 * df(x_k) - x_k * df(x_k1) )/ (df(x_k) - df(x_k1))
        if abs(x_new - x_k) <=tol:
            break
        x_k1 = x_k
        x_k = x_new
    if i >= maxiter:
        convg = False
    else:
        convg = True
        
    plt.figure(1)
    x = np.linspace(-1,2,100)
    f = lambda x: x*x +np.sin(x) + np.sin(10*x)
    plt.plot(x, f(x))
    plt.plot(x_new,f(x_new),'o')
    plt.show()
    return x_new,convg,i


# Problem 4
def backtracking(f, Df, xk, pk, alpha=1, rho=.9, c=1e-4):
    """Implement the backtracking line search to find a step size that
    satisfies the Armijo condition.

    Parameters:
        f (function): A function f:R^n->R.
        Df (function): The first derivative (gradient) of f.
        x (float): The current approximation to the minimizer.
        p (float): The current search direction.
        alpha (float): A large initial step length.
        rho (float): Parameter in (0, 1).
        c (float): Parameter in (0, 1).

    Returns:
        alpha (float): Optimal step size.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    Dfp = Df(xk)
    fx = f(xk)
    
    while (f(xk+alpha*pk) > fx +c*alpha*np.linalg.norm(Dfp)):
        alpha = rho*alpha
    
    return alpha

if __name__ == "__main__":
    #print("booyeah")
    #f =lambda x: np.exp(x)-4*x
    #print(golden_section(f, 0,3))
    #print(opt.golden(f,brack = (0,3), tol = 0.001))
    #df = lambda x : 2*x + 5*np.cos(5*x)
    #d2f = lambda x : 2 - 25*np.sin(5*x)
    #print(opt.newton(df, x0 = 0, fprime = d2f ,tol = 1e-10,maxiter = 500))
    #print(newton1d(df,d2f,-1.3))
    #df = lambda x: 2*x + np.cos(x) + 10*np.cos(10*x)
    #print(secant1d(df,0,1))
    #print(opt.newton(df, x0=1, tol=1e-10, maxiter=500))
    f = lambda x: x[0]**2 + x[1]**2 + x[2]**2
    Df = lambda x: np.array([2*x[0], 2*x[1], 2*x[2]])
    x = anp.array([150., .03, 40.])
    p = anp.array([-.5, -100., -4.5])
    phi = lambda alpha: f(x + alpha*p)
    dphi = grad(phi)
    alpha1, _ = linesearch.scalar_search_armijo(phi, phi(0.), dphi(0.))
    print(alpha1)
    print(backtracking(f,Df,x,p))
    