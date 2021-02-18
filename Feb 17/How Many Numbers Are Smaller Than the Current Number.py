class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        smallCount = [0]*len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    smallCount[i] += 1
        return smallCount