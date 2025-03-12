'''
Given 'n' print data in inverted pyramid fashion


n = 5
1 2 3 4 5 
1 2 3 5 
1 2 3  
1 2   
1



n = 4
1 2 3 4  
1 2 3 
1 2   
1   

'''

def reversePyramid(n):
      for i in range(0,n+1):
        for j in range(0,n-i):
            print(j+1, end= " ")
        print("")
reversePyramid(5)