class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0

        for i in sorted_nums:
            if i == count:
                count+=1 
            else:
                return count
        return count

