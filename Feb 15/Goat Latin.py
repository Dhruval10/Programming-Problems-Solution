class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        answer = ''
        i = 0
        for string in S.split():
            if string[0].lower() in ['a','e','i','o','u']:
                answer += string + 'maa' + 'a'*i  + ' '
            else:
                answer += string[1:] + string[0] + 'maa' + i*'a'  + ' '
            i += 1
        
        return answer.rstrip()