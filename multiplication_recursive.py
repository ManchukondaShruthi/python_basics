def multiplicationrec(a,b):
    if b == 0:
        return 1
    elif b > 0:
        return a * multiplicationrec(a, b-1)
print(multiplicationrec(5,3))