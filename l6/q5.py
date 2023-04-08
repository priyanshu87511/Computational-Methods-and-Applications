import numpy as np
from scipy.integrate import solve_ivp as sivp
from matplotlib import pyplot as plt, patches
import math
from matplotlib.animation import FuncAnimation 

G = 6.67 * (10**-11)

# function to calculate the acceleration of each particle
def fdd(r1, r2, r3):
    # calculate the distance between particles and take max with 5 to avoid division by zero
    nrm = max(5, (np.linalg.norm(r2 - r1)))
    nsm = max(5, (np.linalg.norm(r3 - r1)))
    # calculate the acceleration
    rdd = ((r2 - r1) / (nrm ** 3)) + ((r3 - r1) / (nsm ** 3))
    return rdd

# function to solve the differential equations of the system
def solve(x, y):
    r11, r12, r21, r22, r31, r32, v11, v12, v21, v22, v31, v32 = y
    r1, r2, r3 = np.array([r11, r12]), np.array([r21, r22]), np.array([r31, r32])
    v1, v2, v3 = [v11, v12], [v21, v22], [v31, v32]
    # calculate the acceleration for each particle
    d1, d2, d3 = fdd(r1, r2, r3), fdd(r2, r1, r3), fdd(r3, r1, r2)
    return [*v1, *v2, *v3, *d1, *d2, *d3]

# function to calculate the variables of the system for plotting
def variables_plot(r, v, T ,m1 = 1, m2 = 1, m3 = 1):
    mass1 = m1
    mass2 = m2
    mass3 = m3
    r1, r2, r3 = r
    v1, v2, v3 = v
    t = np.linspace(0, T, 1000)
    # solve the differential equations
    sol = sivp(fun = solve, t_span=[0, T], y0=[*r1, *r2, *r3, *v1, *v2, *v3], t_eval=t)
    # return the variables for plotting
    r11 = sol.y[0]
    r12 = sol.y[1]
    r21 = sol.y[2]
    r22 = sol.y[3]
    r31 = sol.y[4]
    r32 = sol.y[5]
    return [sol.t, r11, r12, r21, r22, r31, r32]

# calculate the variables for plotting
l = variables_plot([[0,0], [1.73,1], [1.73,-1]], [[0, 0], [0, 0], [0,0]], 1000)

# create the figure and axis for the animation
fig = plt.figure()
axis = plt.axes(xlim=(-1, 3), ylim=(-2, 2)) 

# create the circles for the particles
circle1 = patches.Circle((0, 0), radius=0.05, color='r')
circle2 = patches.Circle((0, 0), radius=0.05, color='b')
circle3 = patches.Circle((0, 0), radius=0.05, color='green')

# data which the line will 
# contain (x, y)
def init(): 
    # initialize circle object
    circle1.set_center((0, 0))
    circle2.set_center((0, 0))
    circle3.set_center((0, 0))
    axis.add_patch(circle1)
    axis.add_patch(circle2)
    axis.add_patch(circle3)
    return [circle1, circle2, circle3]
   
def animate(i):
    # while we have list elements greater than i
    if i < len(l[0]):
        circle1.set_center((l[1][i], l[2][i]))
        circle2.set_center((l[3][i], l[4][i]))
        circle3.set_center((l[5][i], l[6][i]))
        return [circle1, circle2, circle3]

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=100, blit=True)

plt.grid(True)   
plt.show()
anim.save('circle.gif', writer='ffmpeg', fps=5)