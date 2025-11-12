'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

'''
example: 
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeros(nums):
    pos = 0
    for i in nums:
        if i != 0:
            nums[pos] = i
            pos += 1

    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums

nums = [0,1,0,3,12]
print(moveZeros(nums))