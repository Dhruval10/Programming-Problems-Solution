class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        def up_dfs(row,col):
            if col < 0 or col >= len(board[0]) or board[row][col] == '.':
                return 
            board[row][col]='.'
            up_dfs(row,col-1)
            up_dfs(row,col+1)
        def right_dfs(row,col):
            if row < 0 or row >= len(board) or board[row][col] == '.':
                return 
            board[row][col]='.'
            right_dfs(row+1,col)
            right_dfs(row-1,col)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    count += 1
                    if j+1 < len(board[0]) and board[i][j+1] == "X":
                        up_dfs(i,j)
                    elif i+1 < len(board) and board[i+1][j] == "X":
                        right_dfs(i,j)
        return count
