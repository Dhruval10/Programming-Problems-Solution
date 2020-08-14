class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ret = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ret = nums[i]
                break
        return ret
