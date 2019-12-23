# Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        dct = {}
        len_1 = 0
        len_2 = 1
        
        i, j = 0, 0
        while j < len(s):
            if s[j] not in dct:
                dct[s[j]] = 1
                len_1 += 1
                j += 1
                if len_1 >= len_2:
                    len_2 = len_1
            else:
                while s[j] in dct:
			    del dct[s[i]]
			    i += 1
			    len_1 -= 1
        
        return max(len_1, len_2)