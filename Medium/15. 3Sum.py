from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums, i, res):
            seen = set()
            j = i + 1
            
            while j < len(nums):
                compliment = -nums[j] - nums[i]
                if compliment in seen:
                    res.append([nums[i],compliment,nums[j]])
                    while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                seen.add(nums[j])
                j += 1
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i] != nums[i-1]:
                twoSum(nums, i, res)
        return res
