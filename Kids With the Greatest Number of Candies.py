class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return_ans = []
    
        max = 0
        
        for i in candies:
            if i > max:
                max = i

        for i in candies:
            if (i + extraCandies) >= max:
                return_ans.append(True)
            else:
                return_ans.append(False)
        return return_ans
