'''
Given n, find sum of digits of a number using recursion

example : 872
result : 17
explanation : 8 + 7 + 2 = 17  


example : 100
result : 1 
explanation : 1 + 0 + 0 = 1  

'''

# def recursive_sum_of_digits(n):
#     pass

# n = 872
# print(recursive_sum_of_digits(n))


# def sumofdigits(n):
#     if n == 0:
#         return 0
#     else:
#         sum = 0
#         reminder = n % 10
#         sum = sum + reminder
#         n = n // 10
#     return sumofdigits(sum)
# n = 768
# print(sumofdigits(n))


def sumofdigits(x):
    if x < 10:
        return x
    else:
        return x%10 + sumofdigits(x//10)
print(sumofdigits(768))