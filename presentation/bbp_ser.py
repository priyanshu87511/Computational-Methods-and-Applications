import decimal
import matplotlib.pyplot as plt

def bbp(n):
    pi = 0
    
    for k in range(n):
        term = ( 4/(8*k+1) - 2/(8*k+4) - 
            1/(8*k+5) - 1/(8*k+6) ) / (16 ** k)
        term = term
        pi += term

    return pi

print(bbp(100)) # prints '3.243f6a8885a3'
