class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        if len(words) == 1:
            return True
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                length = min(len(words[i]),len(words[j]))
                for k in range(length):
                    if k == length-1 and len(words[i]) > len(words[j]):
                        if order.index(words[i][k]) < order.index(words[j][k]):
                            break
                        else:
                            return False
                    elif order.index(words[i][k]) < order.index(words[j][k]):
                        break
                    elif order.index(words[j][k]) < order.index(words[i][k]):
                        return False
        return True
