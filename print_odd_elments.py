'''
Print elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: The list index always starts at 0

Expected output:

20 40 60 80 100
'''

def printoddindexpositions(x):
    for i in range(0, len(x),1):
        if i % 2 != 0:
            print(x[i])
printoddindexpositions([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
