class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        for i in range(0,len(s),2*k):
            s = s[:i] + s[i:i+k][::-1] + s[i+k:]
        return s
