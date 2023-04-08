# importing required libraries
from matplotlib import pyplot as plt, patches
import numpy as np
import math
from matplotlib.animation import FuncAnimation

# function to evaluate theta, velocity, ac, hvalue, L for a given time step
def evaluate(theta, velocity, ac, hvalue, L):
    return [theta + velocity * hvalue, velocity + ac * hvalue, -(9.8 * math.sin(theta)) / L, hvalue, L]

# function to calculate pendulum motion based on initial angle, velocity, time step, length, and time
def pendulum(theta, velocity, hval, l, time):
    all = [[theta, velocity, 0, hval, l]]
    for i in range((int)(time/hval)):
        all.append(evaluate(all[i][0], all[i][1], all[i][2], all[i][3], all[i][4]))
    return all

# calculate pendulum motion for given parameters
l = pendulum(math.pi / 4, 0, 0.01, 1, 10)

# create a figure and set axis limits
fig = plt.figure()
axis = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

# initialize line and circle objects
line, = axis.plot([], [], lw=3)
circle = patches.Circle((0, 0), radius=0.1, color='red')

# function to initialize animation
def init(): 
    line.set_data([], [])
    circle.set_center((0, 0))
    axis.add_patch(circle)
    return [line, circle]

# function to animate each frame of the pendulum
def animate(i):
    if i < len(l):
        theta = l[i][0]
        ycord = -l[i][4] * math.cos(l[i][0])
        xcord = l[i][4] * math.sin(l[i][0])
        x = np.linspace(0, xcord, 1000)
        y = np.linspace(0, ycord, 1000)
        line.set_data(x, y)
        circle.set_center((xcord, ycord))
        return [line, circle]

# create animation object and save to file
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=5, blit=True)
plt.grid(True)   
plt.show()
anim.save('PenduluM.gif', writer='ffmpeg', fps=30)
