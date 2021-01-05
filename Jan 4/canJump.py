class Solution:
    def canJump(self, nums: List[int]) -> bool:    
        
        max1, last = 0, len(nums) - 1
        
        i = 0
        
        while i <= max1 and max1 < last:
            
            max1 = max(max1, nums[i] + i)
            
            i += 1
        
        return max1 >= last