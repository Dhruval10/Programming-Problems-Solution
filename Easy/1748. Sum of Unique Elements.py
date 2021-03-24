from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        unique_dict = defaultdict(int)
        
        for i in range(len(nums)):
            unique_dict[nums[i]] += 1
        
        total_sum = 0
        
        for key, val in unique_dict.items():
            if val == 1:
                total_sum += key
        
        return total_sum
