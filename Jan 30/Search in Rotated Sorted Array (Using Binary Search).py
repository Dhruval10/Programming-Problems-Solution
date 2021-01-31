class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low , high = 0, len(nums)-1
        
        while low <= high:
            if not nums:
                return -1
            mid = (high + low)//2
            # Check if target is present at mid or not
            if nums[mid] == target:
                return mid
            # Check if target is present in 1st half
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            # If target is not in 1st half, it must be in 2nd half
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        # If our program comes till here, means it hasn't found any solution, in that case return -1
        return -1
