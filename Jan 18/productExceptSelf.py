class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = []
        multiplier = 1
        for i in range(len(nums)):
            products.append(multiplier)
            multiplier *= nums[i]
        
        multiplier = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= multiplier
            multiplier *= nums[i]
        
        return products
