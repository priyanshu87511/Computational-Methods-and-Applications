import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import math

# Define the system of equations
def f(x):
    x1, x2, x3 = x
    f1 = 3*x1 - math.cos(x2*x3) - 3/2
    f2 = 4*(x1**2) - 625*(x2**2) + 2*x3 - 1
    f3 = 20*x3 + math.exp(-x1*x2) + 9
    return [f1, f2, f3]

# Calculate the Jacobian matrix of the system of equations
def jacobian(x):
    x1, x2, x3 = x
    r1 = [3, x3*math.sin(x2*x3), x2*math.sin(x2*x3)]
    r2 = [8*x1, -1250*x2, 2]
    r3 = [-x2*math.exp(-x1*x2), -x1*math.exp(-x1*x2), 20]
    m = [r1, r2, r3]
    return m

# Implement the Newton-Raphson method to solve the system of equations
def newtonraphson(x0, it):
    # Check the input arguments
    if(type(x0) != list and type(x0) != tuple):
        raise Exception("It should be list or tuple")
    if(len(x0) != 3):
        raise Exception("Expected three values")
    if(it <= 0):
        raise Exception("Iterations should be positive")
    
    lst = [] # Create a list to store the norm of f(x) at each iteration
    ite = [] # Create a list to store the iteration numbers
    for itr in range(it + 1):
        lst.append(la.norm(x0)) # Append the norm of f(x) to the list
        ite.append(itr) # Append the iteration number to the list
        
        # Calculate the next approximation of x using the Newton-Raphson method
        x = x0 - la.inv(jacobian(x0)) @ f(x0)
        x0 = x # Update the current approximation of x
    
    print(x0) # Print the final approximation of x
    plt.plot(ite, lst, color='r', label="newton raphson") # Plot the norm of f(x) against the iteration number
    plt.legend()
    plt.title("∥f (xk)∥ against iterations")
    plt.xlabel("iteration")
    plt.ylabel("∥f (xk)∥")
    plt.grid(True)
    plt.savefig("q5.jpg") # Save the plot to a file
    plt.show() # Show the plot

newtonraphson([1,2,3], 20) # Call the function to solve the system of equations
