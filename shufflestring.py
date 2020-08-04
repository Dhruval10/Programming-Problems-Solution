import sys
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # for i in range(len(s)):
        zipped = zip(s,indices)
        
        zipped = list(zipped)
        sort1 = sorted(zipped, key = lambda x: x[1])
        # output = 
        str1 = ''
        for char in sort1:
            str1+=char[0]
        return str1
