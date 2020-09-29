class Solution:
    def countN(number):
        return number[-1] + number[-2]
    
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        # num1 = 1
        # num2 = 2
        total = 0
        if n == 1:
            return steps[0]
        if n == 2:
            return steps[1]
        else:
            for i in range(2,n):
                steps.append(Solution.countN(steps))
                # total += countN()
            return steps[-1]
