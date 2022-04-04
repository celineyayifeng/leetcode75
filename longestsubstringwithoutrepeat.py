class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charset: #right window starts move
                # print(s[right])
                charset.remove(s[left]) # filter duplicate with set and shrink window
                left += 1 # left window moves
                
            charset.add(s[right])
            res = max(res, right - left + 1) #range of farthest right and left window 
        return res
    
# time complexity: O(n)
# space complexity: O(n)
