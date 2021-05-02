class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        shuffeled = []
        
        for i in range(len(nums)//2):
            shuffeled.append(nums[i])
            shuffeled.append(nums[i+(len(nums)//2)])
        
        return shuffeled
