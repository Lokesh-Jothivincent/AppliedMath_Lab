# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name> Lokesh
<Class> Mth 520
<Date> 2/5/21
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg
from scipy import linalg as la
import numpy as np
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    q,r = la.qr(A,mode = "economic")
    b =np.dot(np.transpose(q),b)
    x_cap = la.solve_triangular(r,b)
    return x_cap


# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    #raise NotImplementedError("Problem 2 Incomplete")
    data = np.load('housing.npy')
    A = list()
    B = list()
    for each in data:
        A.append([each[0],1])
        B.append(each[1])

    A = np.array(A)
    B = np.array(B)
    #over determined system so least square solution
    #call least_squares(A,B)
    x_cap = least_squares(A,B)
    print(x_cap)
    #plotting the data points and the least squares line
    plt.figure(1)
    plt.plot(A[:,0],B,marker = 'o',label = 'Data Points')
    plt.plot(A[:,0],  x_cap[0]* A[:,0]+x_cap[1], label = 'Least squares fit')
    plt.legend (loc = 'upper left')
    plt.show()
    return x_cap


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    #extracting data
    data = np.load('housing.npy')
    year = list()
    index = list()
    for each in data:
        year.append(each[0])
        index.append(each[1])
    year  = np.array(year)
    index = np.array(index)
    #vandermonde matrix of 3,6,9,12
    A3 = np.vander(year,3)
    A6 = np.vander(year,6)
    A9 = np.vander(year,9)
    A12 = np.vander(year,12)
    #least squarwes solution using scipy least squares routine
    #la.lstsq()[0] returns the x_cap
    x3 = la.lstsq(A3,index)[0]
    x6 = la.lstsq(A6,index)[0]
    x9 = la.lstsq(A9,index)[0]
    x12 = la.lstsq(A12,index)[0]
    #fitting a ploynomial using the above results
    fit3 =np.poly1d([x3,1])
    fit6 =np.poly1d([1,1,1,1,1,1])
    fit9 =np.poly1d([1,1,1,1,1,1,1,1,1])
    fit12 =np.poly1d([1,1,1,1,1,1,1,1,1,1,1,1])
    #comparing solutions with polynomial_fit
    #plotting
    new_x = np.linspace(0,16)
    coeff = np.polyfit(year,index,3)
    poly = np.poly1d(coeff)
    new_y = poly(new_x)


    plt.figure(1)
    plt.subplot(221)
    plt.plot(year,index,marker = 'o',label = 'Data Points')
    plt.plot(new_x,new_y,label = 'polyfit')
    #plt.plot(new_x,fit3(new_x),label = 'my fit')
    #plt.plot(np.linspace(0,16,100),fit3(x3))
    plt.show()


    return year


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    #print('booyah')
    a = np.random.randn(9, 6)
    b= np.random.randn(9,1)
    #print(least_squares(a,b))
    #print(line_fit())
    print(polynomial_fit())
