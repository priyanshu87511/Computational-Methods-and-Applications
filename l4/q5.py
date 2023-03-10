import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# defined the function of fx
def f(x):
    return 2*x*pow(math.e, x**2)

# defined f integrated
def f_integrated(x):
    return pow(math.e, pow(x, 2))

# defined the graph
def graph(val=2):
    # for all values of x upto val
    xvalues = np.arange(0, val, 0.01)
    arg = []
    arg2 = []
    yvalues = []
    quad = []
    romberg = []
    trapezoid = []
    simpson = []
    # for u in xvalues
    for u in xvalues:
        # arguments passed in trapezoid and simpson
        arg.append(f(u))
        arg2.append(u)
        # using various techniques
        yvalues.append(f_integrated(u)-f_integrated(0))
        quad.append(integrate.quad(f, 0, u)[0])
        romberg.append(integrate.romberg(f, 0 ,u))
        trapezoid.append(integrate.trapezoid(arg, arg2))
        simpson.append(integrate.simpson(arg, arg2))
    # plotting the graph with title and legend
    plt.plot(xvalues, yvalues, label = "true area")
    plt.plot(xvalues, quad, label = "quad area", linestyle="dashed")
    plt.plot(xvalues, romberg, label = "romberg area", linestyle="dashdot")
    plt.plot(xvalues, trapezoid, label = "trapezoid area", linestyle="--")
    plt.plot(xvalues, simpson, label = "simpson area", linestyle="dotted")
    plt.xlabel("u value")
    plt.ylabel("area")
    plt.title("Visualize area")
    plt.grid(True)
    plt.legend()
    # showing the figure
    plt.savefig("q5.png")
    plt.show()

# test till where we want
graph(2)