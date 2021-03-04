class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # nums.sort()
        number = len(nums)
        if number == 1:
            if 1 not in nums:
                return 1
            else:
                return 2
        elif number == 0:
            return 1
        
        nums = sorted(list(set(nums)))
        mini = min(nums)
        maxi = max(nums)
        count = 1
        for i  in range(mini, maxi+1):
            if count not in nums:
                return count
            count += 1
        return count