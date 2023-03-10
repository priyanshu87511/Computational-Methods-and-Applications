import numpy as np
import math
import matplotlib.pyplot as plt

# using function graph to plot both derivative functions
def graph():
    # taking 1000 points in the interval
    xvalues = np.arange(0,1,0.001)
    # taking actual and forward_finite values
    actual = []
    forward_finite = []
    # for all values in xvalues finding both the derivatives
    for val in xvalues:
        actual.append(2*val*math.cos(val**2))
        forward_finite.append((math.sin((val+0.01)**2) - math.sin(val ** 2))/ 0.01)
    # plotting the graph with title and legend
    plt.plot(xvalues, actual, label = "actual")
    plt.plot(xvalues, forward_finite, label = "forward_finite difference approximation")
    plt.xlabel("x values")
    plt.ylabel("derivative values")
    plt.title("Visualize derivatives")
    plt.grid(True)
    plt.legend()
    # showing the figure
    plt.savefig("q1.png")
    plt.show()

# test
graph()