class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = [str(i) for i in digits]
        result = str(int("".join(digits)) + 1)

        return [i for i in result]
