#Write a function to check if a given number is a perfect square
# x is an empty list whoch we declared to put the Factors of n
# y is a variable to find out the quiotent

def checkPerfectSquare(n):
    x = []
    y = 0
    z = True
    for i in range(1,n,1):
        if (n%i == 0) and (i != 1):
            x.append(i)
            y = (int(n / i))
            if (y == i):
                return True
    return False
z = checkPerfectSquare(17)
print(z)