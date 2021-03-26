class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        word1 = s[:len(s)//2]
        word2 = s[len(s)//2:]
        
        word1_count = 0
        word2_count = 0
        
        set1 = ['a','e','i','o','u','A','E','I','O','U']
        
        for i in range(len(word1)):
            if word1[i] in set1:
                word1_count += 1
            if word2[i] in set1:
                word2_count += 1
        
        return word1_count == word2_count
