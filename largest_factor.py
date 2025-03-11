#Find largest factor of n otherthan 1 and return it

def largestFactor(n):
    x = []
    y = 0
    for i in range(1,n,1):
        if (n%i == 0) and (i != 1):
            x.append(i)
            # to access last number of a list python notation is -1. Since 0 is the first element of the list -1 would be last number of the list.
            y = x[-1]
            # break
    return y
print(largestFactor(24))




