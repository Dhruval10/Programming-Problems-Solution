class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        
        for arr in accounts:
            sum1 = 0
            for i in arr:
                sum1 += i
            if sum1 > maxi:
                maxi = sum1
        return maxi
