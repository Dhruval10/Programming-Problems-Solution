class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        fin_answer = []
        
        for i in range(n):
            fin_answer.append(nums[i])
            fin_answer.append(nums[i+n])
        
        return fin_answer