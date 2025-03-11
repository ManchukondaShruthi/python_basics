#Find smallest factor of n otherthan 1 and return it

def smallestFactor(n):
    x = []
    for i in range(1,n,1):
        if (n%i == 0) and (i != 1):
            # append will add the value into the list 
            x.append(i)
            x = x[0]
            break
    return x
print(smallestFactor(9))


