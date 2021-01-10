class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        arr = [0]*26
        maxi = -1
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] = i
        for i in range(len(s)):
            maxi = max(arr[ord(s[i]) - ord('a')] -i-1, maxi)
        
        return maxi