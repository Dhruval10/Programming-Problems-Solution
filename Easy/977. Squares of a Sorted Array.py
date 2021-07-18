class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = [0] * len(nums)
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            lnum, rnum = abs(nums[left]), abs(nums[right])
            if lnum >= rnum:
                answer[right-left] = lnum*lnum
                left += 1
            else:
                answer[right-left] = rnum*rnum
                right -= 1
        return answer
