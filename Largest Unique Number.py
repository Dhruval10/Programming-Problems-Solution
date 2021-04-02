from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        
        counts = defaultdict(int)
        
        for i in A:
            counts[i] += 1
        
        count = sorted(counts.items(), key= lambda x:x[0], reverse = True)
        
        for i in range(len(count)):
            if count[i][1] == 1:
                return count[i][0]
        return -1
