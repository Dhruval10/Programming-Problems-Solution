class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Define two states, current and next
        current = [[0 for _ in range(n)] for _ in range(n)]
        next1 = [[0 for _ in range(n)] for _ in range(n)]
        current[row][column] = 1
        
        # Mark all possible moves of a knight in chessboard
        all_pos = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(2,-1),(1,-2)]
        
        for _ in range(k): # K moves
            for i in range(n): # board of size n * n
                for j in range(n): # start from cell [0,0] and check if current value is non-zero
                    if current[i][j] != 0:
                        for pos in all_pos: # For each valid moves from all_pos, add values to next steps
                            temp_x = i + pos[0]
                            temp_y = j + pos[1]
                            if 0 <= temp_x < n and 0 <= temp_y < n: # If the knight is inside the board, then add current value divide by 8. 
                                next1[temp_x][temp_y] += (current[i][j] / 8) # We divided it by 8 as there are total 8 possibilities
            current, next1 = next1, [[0 for _ in range(n)] for _ in range(n)] # Assign next as current and redefine next as empty array. Now, we'll again fill this next array with values of current
        
		# Find total probability of the last state. That'll be current as we just swapped current & next!!
        total_sum = 0
        for item in current:
            total_sum += sum(item)
        return total_sum
