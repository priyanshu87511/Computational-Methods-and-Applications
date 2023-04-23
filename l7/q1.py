import math
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 

# Function to compute the initial temperature distribution
def initial(h):
    x0 = []
    x = 0
    while(x <= 1):
        x0.append(math.exp(-x))
        x += h
    return x0

# Function to compute the temperature distribution at each time step
def induction(h, k, x0):
    x = [0]
    for i in range(1, len(x0) - 1):
        x.append(((x0[i-1] - 2*x0[i] + x0[i+1])/(h**2))*k + x0[i])
    x.append(0)
    return x

# Function to compute the temperature distribution at each time step for a given number of iterations
def iteration(h, k, it):
    x = [initial(h)]
    for itr in range(it):
        x.append(induction(h, k, x[itr]))
    return x

# Function to compute the spatial grid points
def Xplot(h):
    x0 = []
    x = 0
    while(x <= 1):
        x0.append(x)
        x += h
    return x0

# Function to compute the temperature distribution for a range of iterations
def f(h, k, it):
    # raise exception
    if(k/(h**2) > 0.5 or it <= 0):
        raise Exception("Invalid values for variable")
    return Xplot(h), iteration(h, k, it)

# Compute the temperature distribution for a range of iterations
# Time is k * itr
x, ys = f(0.01, 0.00005, 10000)

# Create a plot of the temperature distribution
fig, ax = plt.subplots()

# Initialize the plot with an empty line
line, = ax.plot([], [])

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to animate the plot for each frame
def animate(i):
    plt.title("Temperature plot " + str(i+1))
    plt.xlabel("Length Fraction")
    plt.ylabel("Temperature Fraction")
    y = ys[i]
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=len(ys), init_func=init, blit=True, interval=5)

# Set the x and y limits for the plot
plt.xlim(0, 1)
plt.ylim(0, 1)

# Display the plot
plt.show()

# Save the animation as a GIF file
ani.save("q1.gif")
