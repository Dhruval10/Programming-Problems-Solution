class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        updated_list = []
        i = 0
        while i < len(nums):
            new_arr = [nums[i+1]]*nums[i]
            updated_list.extend(new_arr)
            i += 2
        return updated_list
