class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        a += b
        a = bin(a).replace('0b','')
        return a
