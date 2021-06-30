class Solution:
    def isArmstrong(self, n: int) -> bool:
        newNumber = 0
        length = len(str(n))
        for i in str(n):
            newNumber += int(i)**length
        return newNumber == n
