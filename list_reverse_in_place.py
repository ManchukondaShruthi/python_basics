#Given a list a = [500, 200, 300, 250, 400, 100]
# output should be a = [100, 400, 250, 300, 200, 500]
# in-place means it should not take extra memory. Means the list should be sorted in the same list no new list should be created

def revlist(a):
    for i in range(0,len(a)//2,1):
        temp = a[i]
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = temp
    print(a)
n = [500, 200, 300, 250, 400, 100]
revlist(n)

