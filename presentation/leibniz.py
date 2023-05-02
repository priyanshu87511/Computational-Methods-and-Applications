from matplotlib import pyplot as plt

def leibniz_series(n):
    
    numerator = 1
    denominator = 3
    sign = -1
    sum = 1

    for i in range(3, 2*n, 2):
        sum = sum + (numerator / denominator) * sign
        denominator = i+2
        sign = -1 * sign

    return sum*4

print(leibniz_series(10000))