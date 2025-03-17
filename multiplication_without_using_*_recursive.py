def multiplicationwithoutstart(a,b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiplicationwithoutstart(a,b-1)
print(multiplicationwithoutstart(5,2))