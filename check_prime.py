#Given n, print prime numbers of numbers lessthan n
#prime number - a number which has only two factors 1 and the number itself
x = True
def checkPrime(n):
    for i in range(1,n,1):
        if (n%i == 0) and (i != 1):
            return False
    return True
x = checkPrime(11)
print(x)
