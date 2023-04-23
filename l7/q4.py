# Importing the required library
from matplotlib import pyplot as plt

# Defining the function f(x)
def f(x):
    return x**2 + 4*x + 4

# Defining the derivative of the function f(x)
def f_dash(x):
    return 2*x + 4

# Defining the secant method for root finding
def secant(x_k, x_k1):
    # Handling divide by zero exception
    if((f(x_k) - f(x_k1)) == 0):
        return x_k - f(x_k)*(x_k - x_k1)
    return x_k - f(x_k)*((x_k - x_k1) / (f(x_k) - f(x_k1)))

# Defining the Newton-Raphson method for root finding
def newton_raphson(x_k):
    return x_k - (f(x_k)/f_dash(x_k))

# Defining the function for convergence plotting
def convergence(i1, i2, it):
    # Handling non-positive iteration value
    if(it <= 0):
        raise Exception("Iterations should be positive")
    
    # Initializing the lists to store the iteration, secant method values, and Newton-Raphson method values
    secant_x = []
    newton_raphson_x = []
    itr = []
    i = 0
    i1_secant = i1
    i2_secant = i2
    i1_newton_raphson = i2
    
    # Iterating through the specified number of iterations
    while(i < it):
        i3_secant = secant(i1_secant, i2_secant)
        i3_newton_raphson = newton_raphson(i1_newton_raphson)
        
        # Adding the values to the respective lists
        itr.append(i+1)
        secant_x.append(i3_secant)
        newton_raphson_x.append(i3_newton_raphson)
        
        # Updating the values for the next iteration
        i1_secant = i2_secant
        i2_secant = i3_secant
        i1_newton_raphson = i3_newton_raphson
        i += 1
    
    # Plotting the convergence graph
    plt.plot(itr, secant_x, color='r', linestyle="dotted", label="Secant")
    plt.plot(itr, newton_raphson_x, color='b', linestyle="dotted", label="Newton Raphson")
    plt.legend()
    plt.title("Convergence")
    plt.xlabel("iteration")
    plt.ylabel("X values")
    plt.grid(True)
    
    # Saving the graph as an image file and displaying it
    plt.savefig("q4.jpg")
    plt.show()

# Calling the function with initial guesses, number of iterations, and the function f(x)
convergence(10, 8, 20)
