#find 3 in nums = [1,2,3,4,5,6,7,8,9,10]

def binarysearch(nums, x):
    low = 0
    high = len(nums)-1
    mid = (low + high) // 2
    while(low < high):
        mid = (low + high) // 2
        if x == nums[mid]:
            return mid
        if x > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return nums[mid]
nums = [1,2,3,4,5,6,7,8,9,10]
print(binarysearch(nums, 6.5))