# Given array of integers, nums, and an integer, target, return indices
# of the two numbers that add up to target.
# 
# Each input has exactly one solution, and cannot use the same element twice.
# Solution should be a list of the indices.
#
# For instance,
# 
# nums:
#
#   ->  +-----+-----+-----+-----+
#   ->  |  1  |  5  |  4  |  9  |
#   ->  +-----+-----+-----+-----+
#
# target:
#  
#   ->  5
#
# The expected ouput is [0,2] because nums[0] + nums[2] = 5



class Solution:
    def twoSum(self, nums, target: int):
        ans = {}

        for idx, num in enumerate(nums):
            req = target - num
            if req not in ans:
                ans[num] = idx
            else:
                return [idx, ans[req]]


