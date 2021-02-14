class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict1 = defaultdict(int)
        
        for i in range(len(nums)):
            dict1[nums[i]] += 1
        
        for key, val in dict1.items():
            if val == 1:
                return key
