class Solution:
    def reverse(self, x: int) -> int:
        
        maxi = 2**31
        
        if x < 0:
            x = x * -1
            x = int(str(x)[::-1])*-1
            if x < -maxi:
                return 0
            else:
                return x
        else:
            x = int(str(x)[::-1])
            if x > maxi-1:
                return 0
            else:
                return x