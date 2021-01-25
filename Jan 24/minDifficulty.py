class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n, infinite = len(jobDifficulty), float('inf')
        dp = [[infinite] * n + [0] for i in range(d+1)]
        
        for day in range(1,d+1):
            for i in range(n-day+1):
                max_dp = 0
                for j in range(i,n-day+1):
                    max_dp = max(max_dp, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], max_dp+dp[day-1][j+1])
        return dp[d][0] if dp[d][0] < infinite else -1 
