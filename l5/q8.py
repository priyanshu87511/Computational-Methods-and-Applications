from scipy.fft import fft, ifft
import numpy as np

# defining function multi which takes two arguments a, b which should be int or float
def multi(a, b, truncated = 0):
    if(type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        raise Exception("Int or float values expected")
    # creating their lists for storing their digit
    num1 = []
    num2 = []
    a1 = abs(a)
    b1 = abs(b)
    # defining them to be of equal len
    mx = len(str(a1)) + len(str(b1))
    for i in range(mx):
        num1.append(a1%10)
        a1 = a1 // 10
        num2.append(b1%10)
        b1 = b1 // 10
    # now doing fft on both the lists
    num1 = fft(num1)
    num2 = fft(num2)
    multiplication = num1 * num2
    # lets find inverse after multiplication    
    multiplication = ifft(multiplication)
    # reversing the list
    multiplication = reversed(multiplication)
    # finding what is the product of a and b
    ans=0
    # if we want integer answer then make it 1
    if(truncated):
        # for this adding real parts in ans digit by digit
        for i in multiplication:
            ans = ans*10 + round(i.real)
        ans = int(ans)
        # will get positive answer in these cases
        if((a>=0) and (b>=0)) or ((a<0 and (b<0))):
            print("Computed product", ans)
        # making it negative afterwards
        else:
            print("Computed product", -ans)
        m = (int)(a*b)
        print("Actual Product", m)
    # if it wants float then displaying it
    else:
        # for this adding real parts in ans digit by digit
        for i in multiplication:
            ans = ans*10 + (i.real)
        if((a>=0) and (b>=0)) or ((a<0 and (b<0))):
            print("Computed product", ans)
        else:
            print("Computed product", -ans)
        print("Actual Product", a*b)

# testing    
multi(111111111111111111111111111111111, 142332 ,1)
multi(9.1, 9.25)