# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Lokesh
<Class> Mth 520
<Date> 2/1/21
"""
import numpy as np
from matplotlib import pyplot as plt
#ref....
#https://stackoverflow.com/questions/43469163/how-to-install-colormap-using-pip-for-spyder-python-3-5-on-windows
import matplotlib.colors as mcolors

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    arr_nn = np.random.normal(size=(n,n))
    res_mean = np.mean(arr_nn,axis =1)
    res_var = np.var(res_mean)
    return res_var

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    #raise NotImplementedError("Problem 1 Incomplete")
    input = np.arange(100,1001,100)
    result = [var_of_means(n) for n in input]
    #result = var_of_means(5)
    plt.plot(input, result)
    plt.show()

    return result


# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    #raise NotImplementedError("Problem 2 Incomplete")
    domain = np.linspace(-1*np.pi,np.pi,1000)
    ax = plt.plot(domain,np.sin(domain))
    ax = plt.plot(domain,np.cos(domain))
    ax = plt.plot(domain,np.arctan(domain))
    plt.show()


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    #raise NotImplementedError("Problem 3 Incomplete")
    domain1 = np.arange(-2,1,0.1)
    domain2 = np.arange(1.01,6.01,0.1)
    f = lambda x: 1/(x-1)
    result1 = f(domain1)
    result2 = f(domain2)
    result = np.append(result1, result2)
    plt.plot(domain1,result1,'m:',lw=4)
    plt.plot(domain2,result2,'m:',lw=4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show()
    return result


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    #raise NotImplementedError("Problem 4 Incomplete")
    domain = np.linspace(0,2*np.pi,200)
    res1 = np.sin(domain)
    res2 = np.sin(2*domain)
    res3 = 2*np.sin(domain)
    res4 = 2*np.sin(2*domain)
    fig,ax = plt.subplots(2,2)
    ax[0,0].plot(domain,res1,'g-')
    ax[0,1].plot(domain,res2,'r--')
    ax[1,0].plot(domain,res3,'b--')
    ax[1,1].plot(domain,res4,'m:')
    ax[0,0].set_title('f = sin(x)')
    ax[0,1].set_title('f = sin(2x)')
    ax[1,0].set_title('f = 2sin(x)')
    ax[1,1].set_title('f = 2sin(2x)')
    plt.setp(ax,xlim = [0,2*np.pi],ylim = [-2,2])
    fig.suptitle('Subplots with same axes',fontsize = 20)
    plt.show()
    return 1


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    #raise NotImplementedError("Problem 6 Incomplete")
    cmap1 = mcolors.LinearSegmentedColormap.from_list("n", ["crimson", "gold","steelblue"])
    cmap2 = mcolors.LinearSegmentedColormap.from_list("n", ["blue", "red","green"])
    x_domain = np.linspace(-2*np.pi,2*np.pi)
    y_domain = np.linspace(-2*np.pi,2*np.pi)
    X,Y = np.meshgrid(x_domain,y_domain)
    g = (np.sin(X)*np.sin(Y)) / (X*Y)
    #ploting heat map
    plt.subplot(121)
    plt.pcolormesh(X,Y,g,cmap=cmap1)
    plt.colorbar()
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-2*np.pi,2*np.pi)
    #ploting contour map
    plt.subplot(122)
    plt.contourf(X,Y,g,5,cmap = cmap2)
    plt.colorbar()
    plt.show()
    return 1

if __name__ == "__main__":
    #print(prob1())
    #print(prob3())
    #print(prob4())
    print(prob6())
