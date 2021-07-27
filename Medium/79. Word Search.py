class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # visited = set()
        
        found = []
        
        def dfs(row,col,word,i,target):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or i >= len(target) or (row,col) in visited or target[i] != board[row][col]:
                return 
            # print("In")
            visited.add((row,col))
            word += board[row][col]
            # print("current word:",word)
            if word == target:
                # print(word)
                found.append(word)
            i += 1
            dfs(row+1,col,word,i,target)
            dfs(row,col+1,word,i,target)
            dfs(row-1,col,word,i,target)
            dfs(row,col-1,word,i,target)
            
            visited.remove((row,col))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                # print(i,j,board[i][j],word[0])
                if word[0] == board[i][j]:
                    dfs(i,j,"",0,word)
                    # print("After dfs fun")
                    if len(found) > 0 and found[0] == word:
                        return True
        return False
'''
a b c e
s f e s
A D e e
'''
