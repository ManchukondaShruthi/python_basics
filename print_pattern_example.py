'''
Given 'n' print data in pyramid fashion


n = 5
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5



n = 4
1  
2 2  
3 3 3  
4 4 4 4  

'''

def pyramid(n):
    for i in range(1,n+1,1):
        for j in range(i):
            print(i, end = " ")
        print("")
(pyramid(5))


