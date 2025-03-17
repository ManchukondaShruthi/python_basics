#find 3 in nums = [1,2,3,4,5,6,7,8,9,10] using recurssion


def binarysearch(nums, x, low, high):
    # low = 0
    # high = len(nums)-1
    mid = (low + high) // 2
    if low > high:
        return None
    elif x == nums[mid]:
        return mid
    elif x > nums[mid]:
        low = mid + 1
        return binarysearch(nums, x, low, high)
    elif x < nums[mid]:
        high = mid - 1
        return binarysearch(nums, x, low, high)
nums = [1,2,3,4,5,6,7,8,9,10]
print(binarysearch(nums, 6, 0, 9))



