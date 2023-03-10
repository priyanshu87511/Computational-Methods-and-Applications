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
        if(type(num)!=int or num==0):
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

# test it
r1 = RowVectorFloat([1, 2, 4])
r2 = RowVectorFloat([1, 1, 1])
r3 = r1/2
r3[-1] = 2
print(r3)