class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        i_max = len(board)
        j_max = len(board[0])        
    
        def countNeighbours(i,j, count):
            neighbours = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
            for neighbour in neighbours:
                curr_x = neighbour[0] + i
                curr_y = neighbour[1] + j
                if 0 <= curr_x < i_max and 0 <= curr_y < j_max and board[curr_x][curr_y] == 1:
                    count += 1
            return count
        
        live_array = []
        dead_array = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = countNeighbours(i,j, 0)
                if count in [2,3] and board[i][j] == 1:
                    live_array.append([i,j])
                elif board[i][j] == 0 and count == 3:
                    live_array.append([i,j])
                elif board[i][j] == 1 and count < 2:
                    dead_array.append([i,j])
                elif board[i][j] == 1 and count > 3:
                    dead_array.append([i,j])
        for i,j in live_array:
            board[i][j] = 1
        for i,j in dead_array:
            board[i][j] = 0
