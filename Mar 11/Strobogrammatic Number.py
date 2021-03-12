class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated = ''
        reverse1 = num[::-1]
        for number in reverse1:
            if number in ['0','1','8']:
                rotated += number
            elif number == '6':
                rotated += '9'
            elif number == '9':
                rotated += '6'
            else:
                return False
        return str(rotated) == num