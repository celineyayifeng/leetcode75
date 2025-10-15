class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) 
        
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * right # output value output[3] = 6 x 1 = 6
            right = right * nums[i] # update to the right value 1 x 4 = 4 --> right 
        
        return output
    
        

        
