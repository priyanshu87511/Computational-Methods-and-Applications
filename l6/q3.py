from matplotlib import pyplot as plt, patches
import numpy as np
import math
from matplotlib.animation import FuncAnimation 

def evaluate(theta, velocity, ac, hvalue, L):
    return [theta + velocity * hvalue, velocity + ac * hvalue, -(9.8 * math.sin(theta)) / L, hvalue, L]

def pendulum(theta, velocity, hval, l, time):
    all = [[theta, velocity, 0, hval, l]]
    for i in range((int)(time/hval)):
        all.append(evaluate(all[i][0], all[i][1], all[i][2], all[i][3], all[i][4]))
    return all

l = pendulum(math.pi / 4, 0, 0.01, 1, 10)

# create circle object

# initializing a figure in 
# which the graph will be plotted
fig = plt.figure()
   
# marking the x-axis and y-axis
axis = plt.axes(xlim=(-2, 2), ylim=(-2, 2)) 

# initializing a line variable
line, = axis.plot([], [], lw=3)
circle = patches.Circle((0, 0), radius=0.1, color='red')

# data which the line will 
# contain (x, y)
def init(): 
    line.set_data([], [])
    # initialize circle object
    circle.set_center((0, 0))
    axis.add_patch(circle)
    return [line, circle]
   
def animate(i):
    if i < len(l):
        theta = l[i][0]
        ycord = -l[i][4] * math.cos(l[i][0])
        xcord = l[i][4] * math.sin(l[i][0])
        x = np.linspace(0, xcord, 1000)
        y = np.linspace(0, ycord, 1000)
        # update line and circle objects
        line.set_data(x, y)
        circle.set_center((xcord, ycord))
        return [line, circle]

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=5, blit=True)

plt.grid(True)   
anim.save('PenduluM.gif', writer='ffmpeg', fps=30)
