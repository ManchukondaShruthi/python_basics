'''
Given 'n' print data in pyramid fashion


n = 5
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5



n = 4
1  
1 2  
1 2 3  
1 2 3 4  

'''

def printPatten(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end= " ")
        print("")

printPatten(5)
