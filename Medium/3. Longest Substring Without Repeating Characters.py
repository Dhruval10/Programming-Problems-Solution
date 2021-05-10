class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        max_str = ''
        
        temp_str = ''
        for char in s:
            if char not in temp_str:
                temp_str += char
                max_len = max(max_len,len(temp_str))
            else:
                idx = temp_str.index(char)
                temp_str = temp_str[idx+1:]+char
        return max_len
