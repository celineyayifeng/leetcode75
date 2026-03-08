class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int: 
        # two pointer sliding window  
        left = 0 # pointer of sliding window
        max_length = 0 # value to return
        charset = set() # keep current characters forming the longest string 

        for right in range(len(s)): 
            while s[right] in charset: # if value already exists
                charset.remove(s[left]) # remove the value that already exists 
                left += 1 # move left pointer 
            charset.add(s[right]) 
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
# time complexity: O(n)
# space complexity: O(n)
