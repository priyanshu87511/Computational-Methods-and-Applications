import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math

# Compute the period of the limit cycle for a given value of mu and initial condition y0
def limit_cycle_period(mu, y0, upto):

    # Define the van der Pol equation
    def van_der_pol(x, y):
        dydx = [y[1], mu*(1-y[0]**2)*y[1] - y[0]]
        return dydx
    
    def show(x, y):
        plt.plot(x, y) 
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Van der Pol oscillator")
        plt.savefig("q4.png")
        plt.show()
        
    # Solve the van der Pol equation using solve_ivp
    sol = solve_ivp(van_der_pol, [0, upto], y0)
    # Extract the solution for y
    x = sol.t 
    y = sol.y[0] 
    show(x,y)
    # Extract the corresponding values of t
    # print(x,y,sep="\n")
    crossings = np.where(np.diff(np.sign(y)))[0] 
    # Find the indices of the zero crossings
    # Compute the mean period between the crossings
    time = np.mean(2*np.diff(x[crossings]))
    print("Time period of the limit cycle is", time)

# Compute the period of the limit cycle and print it to the console
T = limit_cycle_period(mu = 2.5, y0 = [0.1, 0.1], upto = 100)