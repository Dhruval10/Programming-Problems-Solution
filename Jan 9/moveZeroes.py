class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[current] == 0:
                nums[i], nums[current] = nums[current], nums[i]
            
            if nums[current] != 0:
                current += 1