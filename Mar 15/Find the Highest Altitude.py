class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current = 0
        maxi = 0
        for i in range(len(gain)):            
            current = current + gain[i]
            maxi = max(maxi, current)
        
        if maxi >= 0:
            return maxi
        else:
            return 0