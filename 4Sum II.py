class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sums ={}
        for i in A:
            for j in B:
                if i+j not in sums:
                    sums[i+j] = 1
                else:
                    sums[i+j] +=1
        count = 0
        for i in C:
            for j in D:
                if -(i+j) in sums:
                    count+=sums[-(i+j)]
        return count
