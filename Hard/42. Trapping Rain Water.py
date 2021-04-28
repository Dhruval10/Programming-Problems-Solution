class Solution:
    def trap(self, height: List[int]) -> int:
        trappedWater = []
        maxi = 0
        for h in height:
            maxi = max(h, maxi)
            trappedWater.append(maxi)
        maxi = 0
        for i in range(len(height)-1,-1,-1):
            maxi = max(maxi, height[i])
            trappedWater[i] = min(trappedWater[i], maxi) - height[i]
        
        return sum(trappedWater)
