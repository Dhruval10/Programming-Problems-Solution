class Solution:
    def isThree(self, n: int) -> bool:
        list1 = []
        i = 1
        while i <= n :
            if (n % i==0) :
                list1.append(i)
            i = i + 1
            if len(list1) > 4:
                return False
        if len(list1) == 3:
            return True
