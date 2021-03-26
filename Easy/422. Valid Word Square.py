class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except:
                    return False
        return True
