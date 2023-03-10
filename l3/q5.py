import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import Akima1DInterpolator, CubicSpline, BarycentricInterpolator
import numpy as np

# Create a figure and axes for the plot
fig, axes = plt.subplots(figsize=(12, 5))

# Define a function to be interpolated
def eval(x):
    return np.tan(x) * np.sin(30 * x) * np.exp(x)

# Generate x and y values for the function
xvalues = np.arange(0, 1, 0.001)
yvalues = eval(xvalues)

# Define the animation function
def animate(i):
    # Increase the number of sample points by 1 each frame
    i += 1
    x = np.array(sorted(np.random.rand(i)))
    
    # adding zero before each list to start the graph with zero
    xs = [0]
    for val in x:
        xs.append(val)
    y = eval(x)
    ys = [0]
    for val in y:
        ys.append(val)
    x = xs
    y = ys
    
    # Clear the plot and set the plot title and axes labels
    axes.clear()
    axes.set_title("Different interpolations of tan(x)⋅sin(30x)⋅eˣ for " + str(i)  + " samples")
    axes.set_xlabel("x")
    axes.set_ylabel("f(x)")
    
    # Plot the true function
    plt.plot(xvalues, yvalues, c="blue", label="True")
    
    # Plot the cubic spline interpolation
    cs = plt.plot([], [], c="red", label="Cubic spline")[0]
    cs.set_data(xvalues, CubicSpline(x, y)(xvalues))
    
    # Plot the Akima interpolation
    ak = plt.plot([], [], c="green", label="Akima")[0]
    ak.set_data(xvalues, Akima1DInterpolator(x, y)(xvalues))
    
    # Plot the barycentric interpolation
    bc = plt.plot([], [], c="purple", label="Barycentric")[0]
    bc.set_data(xvalues, BarycentricInterpolator(x, y)(xvalues))
    
    # Add the legend to the plot
    axes.legend()

# Create the animation object and save it to a GIF file
anim = FuncAnimation(fig, animate, interval=500, frames=35, repeat=False)
anim.save("q5.gif")

# Show the plot
plt.show()
