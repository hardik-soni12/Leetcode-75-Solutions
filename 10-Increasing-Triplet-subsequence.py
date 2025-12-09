'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and 
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''
'''
# example :

Input: nums = [20,100,10,12,5,13]
Output: true
Explanation: Any triplet where i < j < k is valid.
'''

def increasing_Triplet(nums):
    num_i = num_j = float('inf')
    for num in nums:
        if num <= num_i:
            num_i = num
        elif num <= num_j:
            num_j = num
        else:
            return True
    return False

nums = [20,100,10,12,5,13]
print(increasing_Triplet(nums))