class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ans = heapq.nlargest(k,nums)
        
        return ans[-1] if len(nums) >=k else -1