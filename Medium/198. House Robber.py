class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        else:
            
            dp = [0] * length
            
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            
            for i in range(2,length):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[length-1]

'''
    Dhruval
'''
