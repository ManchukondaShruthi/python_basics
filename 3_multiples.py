#print all 3 multiples lessthan n
def get3multiples(n):
    for i in range(0,n,1):
        if i%3 == 0:
             print(i)
print(get3multiples(10))
