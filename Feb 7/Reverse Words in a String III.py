class Solution:
    def reverseWords(self, s: str) -> str:
        
        ans_str = ''
        
        for word in s.split():
            ans_str += word[::-1] + ' '
        
        return ans_str.rstrip()