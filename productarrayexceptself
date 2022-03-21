class Solution:
    def productExceptSelf(self, nums):
        res = [1] * (len(nums))  # initialize an empty array 
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  
            prefix *= nums[i]  # multiply by the next number
        
        
        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix  # postfix multiply prefix already in res
            postfix *= nums[i]
            
        return res
