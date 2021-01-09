class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        a_max = []
        b_max = []
        
        for i in range(len(grid[0])):
            a_count = 0
            b_count = 0
            for j in range(len(grid[0])):
                if grid[i][j] > a_count:
                    a_count = grid[i][j]
                if grid[j][i] > b_count:
                    b_count = grid[j][i]
            a_max.append(a_count)
            b_max.append(b_count)

        ans = 0
        
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                mini = min(a_max[i], b_max[j])
                if grid[i][j] < mini:
                    ans += (mini - grid[i][j])
                    grid[i][j] = mini
        
        return ans