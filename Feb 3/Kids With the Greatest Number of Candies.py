class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max1 = max(candies)
        
        max_candies = []
        
        for candy in candies:
            max_candies.append(candy + extraCandies >= max1)
        
        return max_candies