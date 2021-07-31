from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()
        # Function to check whehter the given cordinates are valid or not. Specifically check for current value is 0 or 2. If 0 or 2 then stop here.
        def is_valid(x,y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y]==2 or (x,y) in visited:
                return False
            visited.add((x,y))
            grid[x][y]=0
            return True

        max_level = 0
        queue = deque()
        for i in range(len(grid)):        # Find 2 in the array and add it as our starting point
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([[i,j],0])
                    
        while queue:                        # While queue is not empty, go to next nodes, level by level
            [x,y],level = queue.popleft()
            max_level = max(max_level,level)
            for dir in [[0,1],[0,-1],[-1,0],[1,0]]:   # Logic to traverse in 4 directions
                temp_x = dir[0] + x
                temp_y = dir[1] + y
                if is_valid(temp_x,temp_y):
                    queue.append([[temp_x,temp_y],level+1])
                    
        for i in range(len(grid)):            # At the end check if there are any 1's in the gird. If yes, then return false as this is the case of undirected graph and we can't reach here.
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max_level
