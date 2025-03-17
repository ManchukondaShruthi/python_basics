#given an array find sum of numbers

# def recursivesum(n):
#     x = 0
#     for i in range(0, n, 1):
#         x = x + i
#     print(x)
# print(recursivesum(6))



'''

nums is a list of elememt
'''

# def iterative_sum(nums):
#     x = 0
#     for i in range(0, len(nums), 1):
#         x = x + nums[i]
#     print(x)
# nums = [1, 4, 5, 10, 8, 6, 7]
# print(iterative_sum(nums))


# def sumofnrecursive(i, nums, n, x):
#     if nums == nums(n+1):
#         return None
#     else:
#         return sumofnrecursive(i, nums, n, x + nums[i])


def sumofnrecursive(nums, start, end):
    if start == end:
        return 0
    else: 
        sum = nums[start]
        start = start + 1
        return  sum + sumofnrecursive(nums, start, end)
nums = [1, 4, 5, 10, 8, 6, 7]   
print(sumofnrecursive(nums, 0, len(nums)))