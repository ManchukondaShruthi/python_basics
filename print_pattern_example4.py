'''
Given 'n' print data in inverted pyramid fashion


n = 5
5 4 3 2 1 
4 3 2 1  
3 2 1  
2 1  
1



n = 4
4 3 2 1  
3 2 1   
2 1  
1  

'''


def invertedPyramidwithReversenumber(n):
 for i in range(0,n):
        for j in range(0,n-i):
            print(n-j-i, end= " ")
        print("")
invertedPyramidwithReversenumber(5)

