class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        def dfs(row,col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == '.':
                return 
            board[row][col]='.'
            dfs(row,col-1)
            dfs(row,col+1)
            dfs(row+1,col)
            dfs(row-1,col)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    count += 1
                    dfs(i,j)
        return count
