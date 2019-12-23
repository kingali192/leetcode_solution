"""
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # answer stolen online, but i put the comments.
        from collections import Counter
        c = Counter(nums) # put all the numbers in a dict
        c = sorted(c.items(), key=lambda x: x[1], reverse=True) # reversed sorted dictionary sorted based on value not key. 
        return [x[0] for x in c[:k]] #return values from the begining to k to display the top k most values. 
        
        
        # My solution not finished kinda broken, left with a dict of tuples sorted on frequency. 
        freq = {}
        ans = []
        if len(nums) < 2:
            return nums
        
        for item in nums:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        
        sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
        return sorted_freq[0][1]
        return len(sorted_freq)