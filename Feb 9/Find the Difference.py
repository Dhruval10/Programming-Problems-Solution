from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        startS = 0
        startT = 0
        
        S = sorted(s)
        T = sorted(t)
        
        while startS < len(s) and startT < len(t):
            if S[startS] == T[startT]:
                startS += 1
                startT += 1
            else:
                break
                
        if len(s) < len(t):
            return T[startT]
        else:
            return S[startS]
