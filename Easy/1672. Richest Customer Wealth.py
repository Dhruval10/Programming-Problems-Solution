class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        richestAmount = 0
        
        for account in accounts:
            richestAmount = max(richestAmount, sum(account))
        
        return richestAmount
