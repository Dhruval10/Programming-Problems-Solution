class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        carry = 0
        
        for i in range(len(nums)):
            carry = nums[i] + carry
            
            nums[i] = carry
            
        return nums