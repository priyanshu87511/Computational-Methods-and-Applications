from matplotlib import pyplot as plt

def nilkantha_series(n):
    sum = 3
    x = [1]
    y = [3]
    start = 2
    sign = 1
    for i in range(1,n):
        sum += (4 / (start * (start +
            1) * (start + 2))) * sign
        start += 2
        sign *= -1
        x.append(i)
        y.append(sum)
    plt.plot(x,y)
    plt.xlabel("Iteration")
    plt.title("Nilkantha")
    plt.ylabel("PI value")
    plt.grid(True)
    plt.ylim(3.1, 3.15)
    plt.show()
    plt.savefig("nilkantha.jpg")
    return sum

pi = print(nilkantha_series(1000))