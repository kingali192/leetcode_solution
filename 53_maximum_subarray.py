"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums
        
        n = len(nums) // 2
        left = nums[:n-1]
        right = nums[n:]
        left_max_sum = 0
        right_max_sum = 0
        
        for j in range(len(right)):
            if right_max_sum + right[j] > right_max_sum:
                right_max_sum = right_max_sum + right[j]
            
    
        for i in left[::-1]:
            if left_max_sum + left[i] > left_max_sum:
                left_max_sum = left_max_sum + left[i]
            
                
        return left_max_sum + right_max_sum
    
# Divide and Conquer

