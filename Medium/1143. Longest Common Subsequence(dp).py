class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        for i,a in enumerate(text1):
            for j,b in enumerate(text2):
                if a != b:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                else:
                    dp[i+1][j+1] = dp[i][j] + 1
        return dp[-1][-1]
