class Solution(object):
    def containsDuplicate(self, nums):
        a = len(nums)
        b = len(set(nums))
        
        if a > b: 
            return True 
        else:
            return False
