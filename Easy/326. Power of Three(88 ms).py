class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num1 = 1
        while num1 <= n:
            if num1 == n:
                return True
            num1 *= 3
        return False
