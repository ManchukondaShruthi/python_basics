def fibonaci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonaci(x-1) + fibonaci(x-2)
print(fibonaci(3))