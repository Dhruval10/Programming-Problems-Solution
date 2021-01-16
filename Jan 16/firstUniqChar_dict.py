class Solution:
    def firstUniqChar(self, s: str) -> int:
        set1 = {}
        
        for i in range(len(s)):
            if s[i] not in set1:
                set1[s[i]] = 1
            else:
                set1[s[i]] += 1
        
        for val,index in set1.items():
            if index == 1:
                return s.index(val)
        return -1
