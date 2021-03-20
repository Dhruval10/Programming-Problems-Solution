class Solution:
    def isArmstrong(self, n: int) -> bool:
        num1 = n
        array = []
        while n > 0:
            temp1 = n % 10
            array.append(temp1)
            n = n // 10
        
        sum1 = 0
        for i in range(len(array)):
            sum1 += array[i]**(len(array))
        
        if sum1 == num1:
            return True
        else:
            return False
