class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        multiplier = 1
        max_number = nums[0]
        
        for num in nums:
            multiplier *= num
            max_number = max(multiplier,max_number)
            if multiplier == 0:
                multiplier = 1
        
        multiplier = 1
        
        for num in nums[::-1]:
            multiplier *= num
            max_number = max(multiplier,max_number)
            if multiplier == 0:
                multiplier = 1
        
        return max_number
