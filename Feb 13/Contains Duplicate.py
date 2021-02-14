class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        dict1 = defaultdict(int)
        
        for i in range(len(nums)):
            dict1[nums[i]] += 1
        
        occur = list(dict1.values())
        
        if max(occur) > 1:
            return True
        else:
            return False