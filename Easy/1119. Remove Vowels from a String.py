class Solution:
    def removeVowels(self, s: str) -> str:
        
        set1 = ('a','e','i','o','u')
        
        answer = ''
        
        for char in s:
            if char not in set1:
                answer += char
        
        return answer
