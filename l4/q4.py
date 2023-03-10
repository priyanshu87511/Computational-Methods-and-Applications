import math
import numpy as np
import matplotlib.pyplot as plt

# defined the function of fx
def f(x):
    return 2*x*pow(math.e, x**2)

# defined f integrated
def f_integrated(x):
    return pow(math.e, pow(x, 2))

# defined the graph
def graph():
    # for all values of x upto 50
    xvalues = np.arange(1, 50, 1)
    yvalues = []
    # for m in xvalues
    for m in xvalues:
        sum = 0
        # finding the parts and doing the sum in the m intervalgiven
        part = 2/m
        for k in range(1, m+1, 1):
            sum = sum + f(1+part*k) + f(1+(k-1)*part)
        yvalues.append((3-1)*sum/(2*m))
    # plotting the graph with title and legend
    plt.plot(xvalues, yvalues, label = "area as function of m")
    plt.axhline(y=f_integrated(3)-f_integrated(1), label = "true area", c = "orange")
    plt.xlabel("m value")
    plt.ylabel("area")
    plt.title("Visualize area")
    plt.grid(True)
    plt.legend()
    # showing the figure
    plt.savefig("q4.png")
    plt.show()

# test
graph()