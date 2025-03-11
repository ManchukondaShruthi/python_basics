#print all factors of a number 
def factors(n):
    x = []
    for i in range(1,n+1,1):
        if (n%i == 0):
            x.append(i)
    print(x)
x = factors(16)