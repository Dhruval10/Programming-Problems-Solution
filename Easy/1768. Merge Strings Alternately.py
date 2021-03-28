class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        new_word = ''
        
        i = 0
        j = 0
        len1 = len(word1)
        len2 = len(word2)
        
        while i < len1 or j < len(word2):
            if i < len1:
                new_word += word1[i]
                i += 1
            if j < len2:
                new_word += word2[j]
                j += 1
        return new_word
