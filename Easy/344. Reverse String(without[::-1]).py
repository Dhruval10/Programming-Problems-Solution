class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s)//2
        total = len(s)-1
        
        for i in range(mid):
            s[i], s[total-i] = s[total-i], s[i]
