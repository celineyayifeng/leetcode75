Solution #1: 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortnums = sorted(nums)
        min_ind = 0
        max_ind = len(sortnums) - 1

        while sortnums[min_ind] + sortnums[max_ind] != target:
            if sortnums[min_ind] + sortnums[max_ind] < target:
                min_ind += 1
            elif sortnums[min_ind] + sortnums[max_ind] > target:
                max_ind -= 1 
        max_ind2 = len(sortnums) - 1
        
        while sortnums[max_ind] != nums[max_ind2]:
            max_ind2 -= 1
                      
        return [nums.index(sortnums[min_ind]), max_ind2]
      
Solution #2   
    
class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)): 
      new = target - nums[i]
      if new in nums and nums.index(new) != i:
        return [i, nums.index(new)]
