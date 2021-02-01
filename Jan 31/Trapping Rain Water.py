class Solution:
    def trap(self, height: List[int]) -> int:
        
        trappedWater = []
        
        left = 0
        
        for i in range(len(height)):
            left = max(left, height[i])
            trappedWater.append(left)
        
        right = 0
        
        for i in range(len(height)-1,-1,-1):
            right = max(right, height[i])
            trappedWater[i] = min(right, trappedWater[i]) - height[i]
        
        return sum(trappedWater)