class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                sum1 = sum(nums)
                missing_num = (len(nums) * (len(nums)+1)//2) - (sum1 - nums[i])
                return [nums[i], missing_num]
            else:
                pass
