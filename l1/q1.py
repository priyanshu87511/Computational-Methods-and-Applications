# libraries imported for stirling value calculation and plotting graph respectively
import math
import matplotlib.pyplot as plt

# function created to return logarithmic value of stirling value
def log_stirling(n):
    val = math.log (math.sqrt(2 * math.pi * n)) + (n * math.log (n/math.e))
    return val

# initialising values
log_fact = 0
factorial = []
stirling_val = []
values = []

# moving all upto 1000000
for value in range (1, 10**6):

    # calculation of log value of factorial and using appropriate log identities and append in factorial list
    log_fact += math.log (value)
    factorial.append(log_fact)

    # appending stirling values and indices in respective list
    stirling_val.append(log_stirling(value))
    values.append(value)
    
# plotting stirling and factorial respectively
plt.plot(values, stirling_val, label = "stirling", c = "yellow")
plt.plot(values, factorial, label = "factorial", linestyle = "dotted", c = "black")

# adding labels and title of the graph
plt.legend()
plt.title("stirling approximation of factorial")
plt.xlabel("numbers")
plt.ylabel("stirling and factorial values")

# showing it in q1.png
plt.savefig("q1.png")
# showing the graph
plt.show()