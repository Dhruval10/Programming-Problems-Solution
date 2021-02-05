class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jwels_map = defaultdict(int)
        
        for str1 in stones:
            jwels_map[str1] += 1
        
        count = 0
        
        for str1 in jewels:
            if str1 in jwels_map:
                count += jwels_map[str1]
        
        return count