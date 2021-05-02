class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxi = 0
        
        for i in range(len(candies)):
            if candies[i] > maxi:
                maxi = candies[i]
        
        happyKid = []
        
        for candy in candies:
            if candy + extraCandies >= maxi:
                happyKid.append(True)
            else:
                happyKid.append(False)
        return happyKid
