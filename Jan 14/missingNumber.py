class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    
        sum1 = sum(nums)
        total = len(nums)*(len(nums)+1) // 2
        
        return total - sum1

'''
        min1 = 0
        nums = sorted(nums)
        curr = 0
        while min1 < len(nums):
            if min1 != nums[curr]:
                return min1
            else:
                min1 += 1
                curr += 1
            
        return min1
'''
