from scipy.integrate import quad
import math
import numpy as np
import matplotlib.pyplot as plt

# using e power x as a function
def fn(x):
    return math.e**x

# finding ak value to be used for sn
def ak(k):
    # finding the integrand and integrating and returning the value of ak
    integrand = lambda x : fn(x) * math.cos(k*x)
    ax = quad(integrand, -math.pi, math.pi)[0]
    return ax/math.pi

# doing similarly for bk after taking the k 
def bk(k):
    integrand = lambda x : fn(x) * math.sin(k*x)
    ax = quad(integrand, -math.pi, math.pi)[0]
    return ax/math.pi

# finding sn for a particular x and n
def sn(n,x):
    # moving with the formula given for sn
    s = ak(0) / 2
    # computing both of the sigma for 1 to n
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        sum1 += ak(i)*math.cos(i*x)
        sum2 += bk(i)*math.sin(i*x)
    # returning sn
    return sum1 +s+ sum2

# defining fourier function
def fourier(n):
    # checking if type is int 
    if(type(n) != int):
        raise Exception("Type should be int")
    # checking if n is greater than 0
    if(n<0):
        raise Exception("Expected non-negative integer")
    # for 100 points
    num = 100
    # finding 100 points in range of -pi to pi
    xpts = np.arange(-math.pi, math.pi, 2*math.pi/num)
    # computing its sn and e power x values for all points in xpt
    ypts = []
    ypts2 = []
    for pt in xpts:
        ypts.append(sn(n, pt))
        ypts2.append(fn(pt))
    # printing the coefficients from 0 to n
    print("Coefficients are as follows")
    print("k", "ak", "bk")
    for i in range(n+1):
        print(i, ak(i), bk(i))
    # plot
    plt.plot(xpts, ypts, label="fourier")
    plt.plot(xpts, ypts2, label="e power x")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.title("Fourier approximation of e power x")
    plt.legend()
    plt.grid(True)
    # saving the figure
    plt.savefig("q7.png")
    plt.show()
    
# test
fourier(10)