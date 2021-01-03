class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value1 = 0
        value2 = 0
        
        for i in num1:
            value1 = value1 * 10 + (ord(i) - ord('0'))
        
        for j in num2:
            value2 = value2 * 10 + (ord(j) - ord('0'))
        
        return str(value1 * value2)