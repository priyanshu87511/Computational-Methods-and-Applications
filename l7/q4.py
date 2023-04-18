from matplotlib import pyplot as plt

def f(x):
    return x**2 + 4*x + 4

def f_dash(x):
    return 2*x + 4

def secant(x_k, x_k1):
    if((f(x_k) - f(x_k1)) == 0):
        return x_k - f(x_k)*(x_k - x_k1)
    return x_k - f(x_k)*((x_k - x_k1) / (f(x_k) - f(x_k1)))

def newton_raphson(x_k):
    return x_k - (f(x_k)/f_dash(x_k))

def convergence(i1, i2, it):
    secant_x = []
    newton_raphson_x = []
    itr = []
    i = 0
    i1_secant = i1
    i2_secant = i2
    i1_newton_raphson = i2
    while(i < it):
        i3_secant = secant(i1_secant, i2_secant)
        i3_newton_raphson = newton_raphson(i1_newton_raphson)
        itr.append(i+1)
        secant_x.append(i3_secant)
        newton_raphson_x.append(i3_newton_raphson)
        i1_secant = i2_secant
        i2_secant = i3_secant
        i1_newton_raphson = i3_newton_raphson
        i+=1
    plt.plot(itr, secant_x, color='r', linestyle="dotted", label="Secant")
    plt.plot(itr, newton_raphson_x, color='b', linestyle="dotted", label="Newton raphson")
    plt.legend()
    plt.title("Convergence")
    plt.xlabel("iteration")
    plt.ylabel("X values")
    plt.grid(True)
    plt.savefig("q4.jpg")
    plt.show()

convergence(10 , 8 , 20)