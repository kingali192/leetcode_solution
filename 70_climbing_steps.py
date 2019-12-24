"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = [1,1]
        if n >= 2:
            for i in range(2, n+1):
                step.append(step[i-1] + step[i-2])
        return step[-1]