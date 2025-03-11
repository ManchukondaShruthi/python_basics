# Find the largest factor with which the first element is being multiplied
def largestFactorImprovised(n):
    x = []
    y = 0
   
    for i in range(1,n,1):
        if n%i == 0 and i != 1:
            x.append(i)
            # if int is not given python by default considers a division result to float.
            y = int(n / x[0])
    return y
print(largestFactorImprovised(24))