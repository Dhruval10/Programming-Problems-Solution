class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxi = 0
        
        for account in accounts:
            temp_sum = sum(account)
            if temp_sum > maxi:
                maxi = temp_sum
        
        return maxi