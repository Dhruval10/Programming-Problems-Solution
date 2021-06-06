class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        count = 0
        
        visited = set()
        
        for string1 in strs:
            if string1 in visited: continue    
            visited.add(string1)
            self.dfs(string1,strs,visited)
            count += 1
        return count
    
    def dfs(self, string1, strs, visited):
        for i in range(len(strs)):
            if strs[i] in visited:
                continue
            if self.isSimilar(strs[i],string1):
                visited.add(strs[i])
                self.dfs(strs[i],strs,visited)
    
    def isSimilar(self, A,B):
        temp_count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                temp_count += 1
            if temp_count > 2:
                return False
        return True
