class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -math.inf
        start = 0
        end = len(height)-1
        
        while start < end:
            local_area = min(height[start],height[end]) * (end-start)
            area = max(local_area, area)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return area
