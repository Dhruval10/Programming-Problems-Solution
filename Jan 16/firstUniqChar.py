class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 1:
            return 0
        else:
            for i in range(len(s)):
                str1 = s[:i] + s[i+1:]
                if s[i] not in str1:
                    return i
            return -1
