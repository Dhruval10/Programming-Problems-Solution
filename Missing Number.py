class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = len(nums)
        number = int(number * (number+1)/2)
        
        num1 = sum(nums)
        
        number = number - num1
        
        return number
