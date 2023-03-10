import numpy as np
import math
import matplotlib.pyplot as plt

# using function graph to plot both derivative functions
def graph():
    # taking 1000 points in the interval
    xvalues = np.arange(0,1,0.001)
    # taking actual and forward_finite values
    actual = []
    f_plus = []
    f_minus = []
    fc = []
    # for all values in xvalues finding three derivatives
    for val in xvalues:
        actual.append(2*val*math.cos(val**2))
        f_plus.append((math.sin((val+0.01)**2) - math.sin(val ** 2))/ 0.01)
        f_minus.append((math.sin((val-0.01)**2) - math.sin(val ** 2))/ -0.01)
        fc.append((math.sin((val+0.01)**2) - math.sin((val-0.01)**2))/ 0.02)
    # making all np arrays
    f_plus = np.array(f_plus)
    f_minus = np.array(f_minus)
    fc = np.array(fc)
    # plotting the graph with title and legend
    plt.plot(xvalues, abs(actual - f_plus), label = "δ+0.01(x) error")
    plt.plot(xvalues, abs(actual - f_minus), label = "δ-0.01(x) error")
    plt.plot(xvalues, abs(actual - fc), label = "δc0.01(x) error")
    plt.xlabel("x values")
    plt.ylabel("absolute error values")
    plt.title("Visualize absolute error")
    plt.grid(True)
    plt.legend()
    # showing the figure
    plt.savefig("q2.png")
    plt.show()

# test
graph()