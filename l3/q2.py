from random import random
import math
from copy import copy

# creating class RowVectorFloat
class RowVectorFloat:
    # initialising a list which we got as argument
    def __init__(self, start = None):
        # if the given type is not of list
        if (type(start) != list):
            raise Exception("Can not create object of this type")
        self.maintain = start

    # print all elements separated wth space
    def __str__(self):
        strng = ""
        for item in self.maintain:
            strng += str(item) + " "
        return strng

    # return length
    def __len__(self):
        return len(self.maintain)

    # return the item at the given index
    def __getitem__(self, index):
        # if the index is not there in the list
        if(index < -len(self.maintain) or index >= len(self.maintain)):
            raise Exception("This index is not in the list")
        return self.maintain[index]

    # set the value at a given index
    def __setitem__(self, index, value):
        # if index is not there in the list
        if(index < -len(self.maintain) or index >= len(self.maintain)):
            raise Exception("This index is not in the list")
        self.maintain[index] = value
        
    # for operators the operations are defined
    def __mul__(self, num):
        # can only multiply by a number
        if(type(num)!=int):
            raise Exception("Cannot multiply")
        for i in range(len(self.maintain)):
            self.maintain[i]*=num
        return self

    # even in case of reverse multiplication answer will be same
    def __rmul__(self, num):
        return self.__mul__(num)

    # we can add two objects of same class
    def __add__(self, l1):
        if(type(l1) != RowVectorFloat or len(l1) != len(self.maintain)):
            raise Exception("Type error or len not matched")
        for i in range(len(self.maintain)):
            self.maintain[i]+=l1[i]
        return self

    def __truediv__(self, num):
        # can only divide by a number non zero
        if(num==0):
            raise Exception("Cannot Divide")
        for i in range(len(self.maintain)):
            self.maintain[i]/=num
        return self

    # even in case of reverse division error will be raised
    def __rtruediv__(self, num):
        raise Exception("Cannot Divide")

    # we can only sub in case of equal length and list type
    def __sub__(self, l1):
        if(type(l1) != RowVectorFloat or len(l1) != len(self.maintain)):
            raise Exception("Type error or len not matched")
        for i in range(len(self.maintain)):
            self.maintain[i]-=l1[i]
        return self

# creating square matrix class
class SquareMatrixFloat:
    # if we got a number then we will make a matrix of all zeroes
    def __init__(self, num = None):
        # in another case raise exception
        if(type(num)!=int):
            raise Exception("Int expected")
        mat = []
        for it in range(num):
            row = RowVectorFloat([0] * num)
            mat.append(row)
        self.mat = mat
        self.num = num

    # printing the matrix
    def __str__(self):
        string = "The matrix is:"
        for it in self.mat:
            string+="\n"+RowVectorFloat.__str__(it)
        return string

    # taking all the probabilities of i!=j to be random between 0 and 1 and others between 0 and n
    def sampleSymmetric(self):
        for it in range(self.num):
            for n in range(self.num):
                rad = random()
                if(it==n):
                    rad*=self.num
                self.mat[it][n] = rad
                
    # converting to rowechelon form
    def toRowEchelonForm(self):
        start = 0
        # for iterations in range of n
        for itr in range(self.num):
            # if number is not 0 then keeping it at place and dividing row by the number
            if(self.mat[itr][start] != 0):
                self.mat[itr]/=self.mat[itr][start]
                for other in range(itr+1, self.num):
                    if(self.mat[other][start] != 0):
                        self.mat[other]/=self.mat[other][start]
                        self.mat[other] = self.mat[other] - self.mat[itr]
                start += 1
                continue
            # else swapping till it gets 1 at the place and then dividing the row by the number
            for swap in range(itr+1, self.num):
                if(self.mat[swap][start] != 0):
                    self.mat[itr], self.mat[swap] = self.mat[swap], self.mat[itr]
                    self.mat[itr]/=self.mat[itr][start]
                    for other in range(itr+1, self.num):
                        if(self.mat[other][start] != 0):
                            self.mat[other]/=self.mat[other][start]
                            self.mat[other] = self.mat[other] - self.mat[itr]
                    start += 1
                    break

    # checking if the diagonal entry is big than sum of all others in the row
    def isDRDominant(self):
        final = True
        for it in range(self.num):
            sum = 0
            for it2 in range(self.num):
                sum += self.mat[it][it2]
            if(sum > 2*self.mat[it][it]):
                final = False
        return final

    # doing jsolve
    def jSolve(self, ans, it):
        # if it is not DRDominant then we can directly give the exception
        if(self.isDRDominant() == False):
            raise Exception("Not solving because convergence is not guranteed")
        # creating the x and e values initialised
        x = [0] * self.num
        e = []
        # for the number of iterations
        for itr in range(it):
            # in jacobi using the formula and calculating the value of new x
            x_new = copy(x)
            for i in range(self.num):
                val = 0
                for j in range(self.num):
                    if(j != i):
                        val+=self.mat[i][j]*x[j]
                x_new[i] = (ans[i] - val)/self.mat[i][i]
            # setting x to be new x
            x = copy(x_new)
            evl = 0
            # checking e by norm 2
            for i in range(self.num):
                val = 0
                for j in range(self.num):
                    val+=self.mat[i][j]*x[j]
                evl+=(val-ans[i])**2
            e.append(math.sqrt(evl))
        return e,x

    # similarly doing gSolve
    def gsSolve(self, ans, it):
        # generating error similarly
        if(self.isDRDominant() == False):
            raise Exception("Not solving because convergence is not guranteed")
        # initialise
        x = [0] * self.num
        e = []
        # using the formula
        for itr in range(it):
            x_new = copy(x)
            for i in range(self.num):
                val = 0
                for j in range(i):
                    val+=self.mat[i][j]*x_new[j]
                for j in range(i+1, self.num):
                    val+=self.mat[i][j]*x[j]
                x_new[i] = (ans[i] - val)/self.mat[i][i]
            x = copy(x_new)
            evl = 0
            # calculating e norm 2
            for i in range(self.num):
                val = 0
                for j in range(self.num):
                    val+=self.mat[i][j]*x[j]
                evl+=(val-ans[i])**2
            e.append(math.sqrt(evl))
        return e,x
            

# test it
# check
s = SquareMatrixFloat(4)
s.sampleSymmetric()
while not s.isDRDominant():
    s.sampleSymmetric()
(e, x) = s.jSolve([1, 2, 3, 4], 10)
print(x)
print(e)
(err1, x1) = s.gsSolve([1, 2, 3, 4], 10)
print(x1)
print(err1)