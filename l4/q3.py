import numpy as np
import math
import matplotlib.pyplot as plt

# returning double derivative
def fdd(x):
    return 2 * (math.cos(x * x) - 2 * x * x * math.sin(x * x))

# returning triple derivative
def ftd(x):
    return -4 * x * (3 * math.sin(x * x) + 2 * x * x * math.cos(x * x))

# using function graph to plot both derivative functions
def graph():
    # taking 1000 points in the interval
    xvalues = np.arange(0,1,0.001)
    # for h values in range of 0 and 1 
    xhvalues = np.arange(0,1,0.01)
    # neglecting 0
    xhvalues = xhvalues[1:]
    # initialising y values
    yhvaluespls = []
    yhvaluesc = []
    ytplusval = []
    ytcval = []
    # for all h
    for h in xhvalues:
        actual = []
        f_plus = []
        f_tplus = []
        ftc = []
        fc = []
        # for all values in xvalues finding both the derivatives
        for val in xvalues:
            actual.append(2*val*math.cos(val**2))
            f_plus.append((math.sin((val+h)**2) - math.sin(val ** 2))/ h)
            fc.append((math.sin((val+h)**2) - math.sin((val-h)**2))/ (h*2))
            e = np.arange(0, h+h/100, h/10)
            # for all values in 0 to h in 100 distributions
            max_tf = 0
            max_tc = 0
            # finding the maximum corresponding error
            for eval in e:
                max_tf = max(max_tf, abs(fdd(val+eval)))
                max_tc = max(max_tc, abs(ftd(val + eval)))
            # appending it in error
            f_tplus.append(max_tf)
            ftc.append(max_tc)
        # making all np arrays
        f_plus = np.array(f_plus)
        fc = np.array(fc)
        f_tplus = np.array(f_tplus)
        ftc = np.array(ftc)
        # finding max values of plus and c in difference
        ytplusval.append(max(f_tplus)*h/2)
        ytcval.append(max(ftc)*h*h/6)
        yhvaluespls.append(max(abs(actual-f_plus)))
        yhvaluesc.append(max(abs(actual-fc)))
    # plotting the graph with title and legend
    plt.plot(xhvalues, yhvaluespls, label = "maximum δ+h(x) error")
    plt.plot(xhvalues, yhvaluesc, label = "maximum δch(x) error")
    plt.plot(xhvalues, ytplusval, label = "maximum theroritical δ+h(x) error")
    plt.plot(xhvalues, ytcval, label = "maximum theoritical δch(x) error")
    plt.xlabel("h values")
    plt.ylabel("maximum absolute error values")
    plt.title("Visualize maximum absolute error")
    plt.legend()
    # showing the figure
    plt.savefig("q3.png")
    plt.show()

# test
graph()