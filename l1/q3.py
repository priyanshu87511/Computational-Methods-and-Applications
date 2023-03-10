import random as rand
import matplotlib.pyplot as plt
import math

# function to plot monte carlo pi with math pi
def estimatePi(precision):
    # initialising 
    pi = []
    actual = []
    it = []
    count_sq = 0
    count_cl = 0
    # for every iteration generating a random co-ordinate 
    for iteration in range (precision):
        xvalue = rand.random()
        yvalue = rand.random()
        # checking if it lies with in the circle
        dist = math.sqrt(xvalue**2 + yvalue**2)
        if(dist <= 1):
            count_cl += 1
        else:
            count_sq += 1
        # suitably appending the values in pi as the monte carlo method
        pi.append((count_cl / (count_sq + count_cl)) * 4)
        # similary in iteration the index of iteration number and actual value of pi in actual
        it.append(iteration+1)
        actual.append(math.pi)
    # plotting maths pi and monte carlo method pi 
    plt.plot(it, pi, label = "maths pi")
    plt.plot(it, actual, label = "monte carlo method")
    # marking the names of x label and y label
    plt.xlabel("Number of points generated")
    plt.ylabel("4 x fraction of points within the circle")
    plt.legend()
    # displaying the grid a
    plt.grid(True)
    plt.savefig("q3.png")
    # showing graph
    plt.show()
    
# checking for some value
estimatePi(500000)