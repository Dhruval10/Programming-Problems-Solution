class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        counter = 0
        nums = sorted(list(set(nums)))
        if(len(nums) == 0):
            return 1
        for i in range(0, len(nums)):
            if(nums[i] > 0):
                counter = counter + 1
                if(counter != nums[i]):
                    return counter
        if(nums[-1] > 0):
            return nums[-1] + 1
        else:
            return 1
        
        
