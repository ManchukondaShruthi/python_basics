#write a function given n which returns sum of numbers upto 'n'
#example- sumofn(4) = 10 //1+2+3+4 = 10

def sumofn(n):
    x = 0
    for i in range(0,n+1,1):
        #  n = (n(n+1))/2
        x = x + i
    return(x)
x = sumofn(8)
print(x)