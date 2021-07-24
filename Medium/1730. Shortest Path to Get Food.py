from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        queue = deque()
        count = 0
        visited = set()
        found = False
        
        def is_valid(row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "X" or (row,col) in visited:
                return False
            visited.add((row,col))
            return True
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    queue.append([[i,j],0])
                    visited.add((i,j))
                    while len(queue) != 0:
                        if len(queue) == 0:
                            return -1
                        [row,col],count = queue.popleft()
                        if grid[row][col] == "#":
                            return count
                        if is_valid(row+1,col):
                            queue.append([[row+1,col],count+1])
                        if is_valid(row-1,col):
                            queue.append([[row-1,col],count+1])
                        if is_valid(row,col+1):
                            queue.append([[row,col+1],count+1])
                        if is_valid(row,col-1):
                            queue.append([[row,col-1],count+1])
                    return -1
