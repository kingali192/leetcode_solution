"""
75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        
        start = 0
        end = len(nums)
        while (start < end):
            if nums[start] == 0:
                popped = nums.pop(start)
                nums.insert(0,popped)
            elif nums[start] == 2:
                popped = nums.pop(start)
                nums.append(popped)
                end -= 1 # since we moved it to the end now we don't have to check that again.
                start -= 1
                
            start += 1
        return nums