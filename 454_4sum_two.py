"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        
        for a in A:
            for b in B:
                dic[a+b] = dic.get(a+b, 0) + 1
        
        # returns the combinations of additions so key is addition value and value is the amount that equal to that. 
        
        for c in C:
            for d in D:
                res += dic.get(-c-d, 0)
                
        return res