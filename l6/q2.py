from matplotlib import pyplot as plt
import math
import numpy as np
from numpy.linalg import tensorsolve as slve
from scipy.integrate import quad

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
        if(type(l1) == int or type(l1) == float):
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

    # show the polynomial in range and passing values of lists of points to be scattered
    def show(self, start, end, label):
        xvalues = []
        val = start
        while(end >= val):
            xvalues.append(val)
            val += 0.01
        yvalues = []
        # for all the values find the y value
        for val in xvalues:
            yvalues.append(self[val])
        # plot the graph there
        plt.plot(xvalues, yvalues, label=label)
        poly = ""
        for i in range(len(self.poly)):
            poly+="+ (" + str(self.poly[i]) + ") x^" + str(i) + " " 
        plt.title("backward eular")
        # plt.scatter(val1, val2, c="r")
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.grid(True)
        plt.ylim(-10,10)
        # plt.savefig("q1.png")
        # plt.show()

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
        # plt.scatter(xvalues, yvalues, color="red")
        # self.show(start,end)
        return self
        
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
        return self
        # plt.scatter(xvalues, yvalues, color="red")
        # self.show(-1,3)
        
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
    

    # this function returns the bestfit polynomial for a tuplelist
    def bestfit(self, tuplelist, n):
        # taking two list for finding xvals and yvals
        xvals = []
        yvals = []
        # for every given point finding their xvalues and yvalues
        for point in tuplelist:
            xvals.append(point[0])
            yvals.append(point[1])
        # finding minimum and maximum values of xvalues
        xmin = xvals[0]
        ymn = xvals[0]
        # for all points in tuplelist finding the xmin and xmax for giving range in show function
        for point in tuplelist:
            xmin = min(xmin, point[0])
            ymn = max(ymn, point[0])
        # finding all values in b
        b = []
        for i in range(n+1):
            yval = 0
            # for all values in points finding the corresponding values of b
            for j in range(len(tuplelist)):
                yval+=yvals[j]*(xvals[j]**i)
            b.append(yval)
        # finding values of a
        a = []
        # for all values in range n+1
        for i in range(n+1):
            # finding a row 
            lst = []
            # finding sigma of x, x2,x^3 whatever required
            for j in range(n+1):
                sum = 0
                for k in range(len(tuplelist)):
                    sum+=xvals[k]**(i+j)
                lst.append(sum)
            # appended the values of lst to a
            a.append(lst)
        # solving it to find coefficients
        xval = slve(a,b)
        xvals = np.sort(xvals)
        # if two points have same x that it cannot be accepted
        for i in range(1,len(xvals)):
            if(xvals[i]==xvals[i-1]):
                raise Exception("Two points with same x can not be accepted for a function")
        # finding the polynomial of xval
        self = Polynomial(xval)
        # self.show(xmin, ymn, xvals, yvals)
        # plotted the graph and returned the polynomial
        return self


    # defining the Legendre polynomial
    def Legendre(self, n = 5):
        # defining polynomial
        poly = Polynomial([1])
        # having polynomial -1 + x^2
        p = Polynomial([-1,0,1])
        # if n is the negative number
        if(n < 0):
            raise Exception("Negative values provided")
        # for i in range of n finding the polynomial for derivation of it
        for i in range(n):
            poly = p*poly
        # again derivating it for n times
        for i in range(n):
            poly = poly.derivative()
        # finding the number for division
        divi = math.factorial(n) * (2**n)
        # finding poly after division
        poly = poly / divi
        self = poly
        # showing graph in this range
        self.show(-1, 1)
        # returning the polynomial
        return self
    
    # finding the chebyshev polynomial of given degree
    def chebychev(self, n = 2):
        # n should be of type int
        if(type(n) != int):
            raise Exception("n should be of type int")
        # dimension can not be negative
        if(n<0):
            raise Exception("dimension can not be negative")
        poly = Polynomial([])
        # if n is 1 we will modify it to this value as given
        if(n==0):
            poly = Polynomial([1])
        if(n==1): 
            poly = Polynomial([0,1])
        # otherwise applying formula for finding n+1 term given previous two terms
        poly1 = Polynomial([1])
        poly2 = Polynomial([0,1])
        # for every value in range of n
        for i in range(1,n,1):
            poly = (Polynomial([0,2])*poly2) - poly1
            poly1 = poly2
            poly2 = poly
        # having the result in poly and displaying it
        self = poly
        return self
    
    # checking orthogonality
    def cheby_orthogonal(self):
        # taking n to be 5
        n = 5
        # initialising matrix
        mat = []
        # for all the values till n from 0
        for i in range(n):
            # defining row
            row = []
            # for all j from 0 to i+1
            for j in range(i + 1):
                # taking integrand of chebyshev of i at x and similarly for j divided by sqrt(1-x**2)
                integrand = lambda x: self.chebychev(i)[x] * self.chebychev(j)[x] / math.sqrt(1 - x**2)
                # appending the integrated value to row
                row.append(quad(integrand, -1, 1)[0])
            # appending the value to row
            mat.append(row)
        # printing the mat
        for r in mat:
            # it can be shown that all values in each row except last element are 0
            for e in r:
                print("{:.2f}".format(e), end="\t")
            print("\n")

# Define the backward Euler method function
def backwardEular(start, end, steps):
    
    if(start > end):
        raise Exception("start is big")
    
    # Define the function being solved
    def func():
        return lambda t,x,step : x / (1 + 2*step)
    
    # Define the actual solution function for comparison
    def actualfunc():
        return lambda t : 5 * math.exp(-2 * t)
    
    # Loop over all step sizes provided
    for step in steps:
        
        # Get the function to be solved
        f = func()
        
        # Initialize arrays to store x and y values
        xvalues = []
        var = start
        while (var <= end):
            xvalues.append(var)
            var += step
        yvalues = [5]
        
        # Use the backward Euler method to solve for y values
        for i in range(0, len(xvalues) - 1):
            yvalues.append(f(xvalues[i], yvalues[i],step))
        
        # Store points as [x, y] pairs for polynomial fitting
        points = []
        for i in range(0, len(xvalues)):
            points.append([xvalues[i], yvalues[i]])
        
        # Fit a polynomial to the points using matrix method and display the result
        poly = Polynomial([])
        poly = poly.fitViaMatrixMethod(points)
        poly.show(start, end, str(step))
    
    # Generate actual values for comparison
    xvalues = np.arange(start, end, 0.1)
    yvalues = []
    actual = actualfunc()
    for val in xvalues:
        yvalues.append([val, actual(val)])
    
    # Fit a polynomial to the actual values using matrix method and display the result
    poly = Polynomial([])
    poly = poly.fitViaMatrixMethod(yvalues)
    poly.show(start, end, "Actual")
    
    # Save and display the plot
    plt.legend()
    plt.savefig("q2.png")
    plt.show()

  

# test
backwardEular(0, 10, [0.1 , 0.5, 1, 2, 3])