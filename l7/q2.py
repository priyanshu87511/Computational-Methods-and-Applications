from matplotlib import pyplot as plt
import math
import numpy as np
from matplotlib.animation import FuncAnimation
import copy

def initial(h):
    # function to create initial grid with zeros
    x0 = []
    x = 0
    while(x<=1):
        x1 = []
        y = 0
        while(y<=1):
            x1.append(0)
            y+=h
        x+=h
        x0.append(x1)
    return x0

xmin = 0
xmax = 0

def induction(h, k, x0, xc, yc):
    # function to apply the induction equation
    def fn(x1,y1):
        return math.exp(-math.sqrt((x1-xc)**2 + (y1-yc)**2)) # Gaussian function
    global xmin, xmax
    xy = copy.deepcopy(x0) # create a deep copy of the grid
    for i in range(1, len(xy) - 1):
        for j in range(1, len(xy[0]) - 1):
            xy[i][j] = (((((x0[i-1][j] - 2*x0[i][j] + x0[i+1][j]) + (x0[i][j-1] - 2*x0[i][j] + x0[i][j+1])))/(h**2) + fn(i,j))*k + x0[i][j])
            xmin = min(xmin, xy[i][j])
            xmax = max(xmax, xy[i][j])
            # update the current cell value using the induction equation
    return xy


def iteration(h, k, it, xc, yc):
    # function to perform the iteration for given number of times
    x = [initial(h)]
    for itr in range(it):
        x0 = copy.deepcopy(x[itr])
        x.append(induction(h, k, x0, xc, yc))
        # create a deep copy of the previous grid and update it using the induction equation
    return x

def Xplot(h):
    # function to create grid of (x,y) points
    x1 = []
    x = 0
    while(x<=1):
        x1.append(x)
        x+=h
    return x1

def f(h, k, it, xc, yc):
    # function to validate inputs and get the grid of (x,y) points and the grid after iteration
    if(k/(h**2) > 0.5 or it <= 0):
        raise Exception("Invalid values for variable") # raise exception if invalid values are passed
    if(xc < 0 or xc > 1 or yc < 0 or yc > 1):
        raise Exception("Invalid values")
    xc *= (1/h)
    yc *= (1/h)
    return Xplot(h), iteration(h, k, it, xc, yc)

# get the (x,y) points and the grid after iteration
xs, ys = f(0.1, 0.0005, 100, 0.5, 0.5)

fig, ax = plt.subplots()

def animate(frame):
    # function to animate the grid
    global xmin, xmax
    ax.clear()
    ax.imshow(ys[frame], cmap='hot', origin='lower', extent=[xmin,xmax,xmin,xmax], animated=True) # display the current grid
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Heatmap")

# setting up the plots
ani = FuncAnimation(fig, animate, frames=len(ys), interval=5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("heatmap")
ani.save("q2.gif")
plt.show()
