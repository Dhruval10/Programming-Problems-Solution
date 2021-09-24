class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0,1,1]
        if n < 3:
            return T[n]
        else:
            for i in range(3,n+1):
                T.append(T[i-1]+T[i-2]+T[i-3])
            return T[n]
