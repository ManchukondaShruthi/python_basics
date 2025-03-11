#Given n, print sum of all numbers lessthan n
#example: print_sum(5) == 1 + 2 + 3 + 4 = 10
def print_sum(n):
    prev_sum = 0
    for i in range (0, n, 1):
        prev_sum = prev_sum + i
    print(prev_sum)
print_sum(5)






