class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
            return index
        except:
            return -1
