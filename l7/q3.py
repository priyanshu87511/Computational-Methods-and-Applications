import math

# define a function to search for the nth root of a number using binary search
def search(a, epsilon, nth):
    # raise an exception if negative values are given
    if(a <= 0 or epsilon <= 0):
        raise Exception("negative values given")
    # base case 1: if nth power is zero, return 1
    if(nth == 0):
        return 1
    # if nth power is negative, convert to positive and take reciprocal of number
    if(nth < 0):
        a = 1/a
        nth = -nth
    # set the left and right boundaries of the search range
    left = 0
    right = max(a,1)
    # perform binary search until the difference between left and right is within epsilon
    while((right - left) > epsilon):
        # set the middle point between left and right
        mid = (left + right)/2
        # check if mid to the nth power is less than or equal to a
        if(pow(mid, nth) <= a):
            # if yes, move the left boundary to mid
            left = mid
        else:
            # if no, move the right boundary to mid
            right = mid
    # return the average of left and right as the nth root of a
    return (left + right)/2

# example usage
root = search(100, 0.00001, 2)
print(root)
