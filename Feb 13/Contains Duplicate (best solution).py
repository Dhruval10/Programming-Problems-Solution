class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Sort an array
        nums.sort()
        
        # check if current number is equal to next number, if yes, return True else check for next number
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            else:
                pass
        return False
#Space: no extra space
#Time: nlog(n)
# Faster than 99% submissions in time
# better than 92% submissions in space
