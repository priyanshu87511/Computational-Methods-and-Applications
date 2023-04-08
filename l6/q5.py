import numpy as np
from scipy.integrate import solve_ivp as sivp

def fdd(r1, r2, r3):
    rdd = ((r2 - r1) / (np.linalg.norm(r2 - r1) ** 3)) + ((r3 - r1) / (np.linalg.norm(r2 - r1) ** 3))
    return rdd

def solve(x, y):
    r11, r12, r21, r22, r31, r32, v11, v12, v21, v22, v31, v32 = y
    r1, r2, r3 = np.array([r11, r12]), np.array([r21, r22]), np.array([r31, r32])
    v1, v2, v3 = [v11, v12], [v21, v22], [v31, v32]
    d1, d2, d3 = fdd(r1, r2, r3), fdd(r2, r1, r3), fdd(r3, r1, r2)
    return [*v1, *v2, *v3, *d1, *d2, *d3]

def variables_plot(r, v, T):
    r1, r2, r3 = r
    v1, v2, v3 = v
    sol = sivp(fun = solve, t_span=[0, T], y0=[*r1, *r2, *r3, *v1, *v2, *v3])
    plotting = []
    r11 = sol.y[0]
    r12 = sol.y[1]
    r21 = sol.y[2]
    r22 = sol.y[3]
    r31 = sol.y[4]
    r32 = sol.y[5]
    return [sol.t, r11, r12, r21, r22, r31, r32]

variables_plot([[0,0], [1.73, 1], [1.73, -1]], [[0, 0], [0, 0], [0,0]], 100)