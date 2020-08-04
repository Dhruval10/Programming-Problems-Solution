class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        for word in s.split():
            output = output + ''.join(reversed(word)) + ' ' 
        return output[:-1]
