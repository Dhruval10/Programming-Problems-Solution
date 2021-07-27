class Trie:
    def __init__(self):
        self.children = {}
        self.isPresent = False
    
    def addNode(self,word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = Trie()
            current = current.children[c]
        current.isPresent = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        found_words = set()
        visited = set()
        
        root = Trie()
        for word in words:
            root.addNode(word)
        
        def dfs(row,col,word,node):
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row,col) in visited or board[row][col] not in node.children):
                return 
            
            visited.add((row,col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isPresent:
                found_words.add(word)
            
            dfs(row+1,col,word,node)
            dfs(row-1,col,word,node)
            dfs(row,col+1,word,node)
            dfs(row,col-1,word,node)
            
            visited.remove((row,col))
            
        # words = list(set(words))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,"",root)
        # print(root.children)
        return list(found_words)

'''
o a t h
e a t

o a b n
o t a e
a h k r
a f l v

'''
