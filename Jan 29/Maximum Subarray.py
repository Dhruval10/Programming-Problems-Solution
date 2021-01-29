class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # The idea is to check whether the previous element is > 0 or not. If it's greater than 0
        # then we can achieve our end goal of getting maximum sum of k consecutive numbers.

        # if the number is negative, then we will skip that number and will check for next number
        
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        
        # Find the max number fron nums since we have already summed numbers and replace them in place.
        return max(nums)