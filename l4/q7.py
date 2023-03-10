from matplotlib import pyplot as plt
import numpy as np
import math
from numpy.linalg import tensorsolve as slve

# creating polynomial class
class Polynomial:
    # initialising with the given coefficients
    def __init__(self, lst = []):
        self.poly = lst
    
    # printing the coefficients
    def __str__(self):
        string = "Coefficients of the polynomial are:\n"
        for i in range(len(self.poly)):
            string += str(self.poly[i])+" "
        return string

    # return length
    def __len__(self):
        return len(self.poly)

        # return the value at the given number
    def __getitem__(self, index):
        ans = 0
        for i in range(len(self.poly)):
            ans+=self.poly[i]*(index**i)
        return ans

    # set the value at a given index
    def __setitem__(self, index, value):
        # if index is not there in the list
        if(index < -len(self.poly) or index >= len(self.poly)):
            raise Exception("This index is not in the list")
        self.poly[index] = value

    # overloading + operator for adding the polynomials
    def __add__(self, l1):
        ans = [0] * max(len(l1), len(self.poly))
        # in case of not adding a polynomial we will raise the error
        if(type(l1) != Polynomial):
            raise Exception("Type error")
        # adding both polynomials upto the min power in both
        for i in range(min(len(l1) , len(self.poly))):
            ans[i]+=l1.poly[i]+self.poly[i]
        # then adding the extra powers of the polynomials if there exists
        if(len(self.poly) == min(len(l1) , len(self.poly))):
            for i in range(min(len(l1) , len(self.poly)), max(len(l1), len(self.poly))):
                ans[i]+=l1.poly[i]
        if(len(l1) == min(len(l1) , len(self.poly))):
            for i in range(min(len(l1) , len(self.poly)), max(len(l1), len(self.poly))):
                ans[i]+=self.poly[i]
        self.poly = ans
        return self
    
    # overloading multiply operator
    def __mul__(self, l1):
        # if integer is given we will do scalar multiplication
        if(type(l1) == int):
            for i in range(len(self.poly)):
                self.poly[i]*=l1
        # in case of polynomial we will multiply the polynomials
        elif(type(l1)==Polynomial):
            ans = [0] * (len(self.poly)+len(l1)-1)
            for i in range(len(self.poly)):
                for j in range(len(l1)):
                    ans[i+j]+=self.poly[i]*l1.poly[j]
            self.poly = ans
        # exception
        else:
            raise Exception("Type Error")
        return self

    # also overload as mul rmul
    def __rmul__(self, l1):
        return self.__mul__(l1)

    # overload - operator
    def __sub__(self, l1):
        return self + (-1)*l1

    # overloading div operator and checking div by 0 condition
    def __truediv__(self, num):
        if(type(num)==int and num!=0):
            for i in range(len(self.poly)):
                self.poly[i]/=num
        else:
            raise Exception("Can't divide")
        return self

    # show the polynomial in range
    def show(self, start, end):
        xvalues = np.arange(start,end,0.01)
        yvalues = []
        # for all the values find the y value
        for val in xvalues:
            yvalues.append(self[val])
        # plot the graph there
        plt.plot(xvalues, yvalues)
        poly = ""
        for i in range(len(self.poly)):
            poly+="+ (" + str(self.poly[i]) + ") x^" + str(i) + " " 
        plt.title("Plot of the polynomial" + poly)
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.grid(True)
        plt.savefig("q4.png")
        plt.show()

    # fit via matrix we used the library of numpy
    def fitViaMatrixMethod(self, lisht):
        a = []
        b = []
        start= lisht[0][0]
        end= lisht[0][0]
        xvalues = []
        yvalues = []
        # finding the a matrix
        for i in range(len(lisht)):
            temp = []
            for j in range(len(lisht)):
                # appending powers of elements for getting the coefficientt
                temp.append(pow(lisht[i][0], j))
            a.append(temp)
            b.append(lisht[i][1])
            start = min(lisht[i][0], start)
            end = max(lisht[i][0], end)
            xvalues.append(lisht[i][0])
            yvalues.append(lisht[i][1])
        # initialised b matrix as the answer matrix to find x
        b = np.transpose(b)
        # found x 
        x = slve(a, b)
        self.poly = x
        # plotting the graph hereby
        plt.scatter(xvalues, yvalues, color="red")
        self.show(start,end)
        
    # doing fit with lagrange
    def fitViaLagrangePoly(self, lisht):
        # initialising vals
        vals = []
        start= lisht[0][0]
        end= lisht[0][0]
        xvalues = []
        yvalues = []
        # using the formula and finding all vals 
        for j in range(len(lisht)):
            self.poly = [1]
            # using formula to multiply with the given poly
            for i in range(len(lisht)):
                if(i!=j and lisht[i][0]!=lisht[j][0]):
                    self*=Polynomial([-lisht[i][0]/(lisht[j][0]-lisht[i][0]), 1/(lisht[j][0]-lisht[i][0])])
            vals.append(self.poly)
            start = min(lisht[j][0], start)
            end = max(lisht[j][0], end)
            xvalues.append(lisht[j][0])
            yvalues.append(lisht[j][1])
        self.poly = []
        # all are added at last according to the formula 
        for j in range(len(lisht)):
            self+=lisht[j][1]*Polynomial(vals[j])
        # plotting the graph hereby
        plt.scatter(xvalues, yvalues, color="red")
        self.show(-1,3)
        
    # adding derivative function
    def derivative(self):
        lisht = []
        # for all terms containing x finding their coefficients after differentiation        lisht = []
        for val in range(1, len(self)):
            lisht.append(self.poly[val] * val)
        # if there is only constant
        if(len(self) == 1):
            lisht.append(0)
        # return the derivative polynomial
        self.poly = lisht
        return self

    # adding area function
    def area(self, start, to):
        # starting with constant which is taken to be zero
        lisht = [0]
        # integrated coefficients are appended in the list
        for val in range(0, len(self)):
            lisht.append(self.poly[val] / (val + 1))
        #   returning their differences which is the area under polynomial
        self.poly = lisht
        return self[to]-self[start]

# test
sinx = []
# finding series of sinx
it = 1
for val in range(1, 15, 2):
    sinx.append(0)
    sinx.append(it/math.factorial(val))
    it = it * -1
sinx = Polynomial(sinx)
# finding series of ex
ex = []
for val in range(0, 15, 1):
    ex.append(1/math.factorial(val))
ex = Polynomial(ex)
# multiplying
exsinx = ex * sinx
# printing area
area = exsinx.area(0,1/2)
print(area)