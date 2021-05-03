class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        js_dict = collections.defaultdict(int)
        
        for i in range(len(stones)):
            js_dict[stones[i]] += 1
        
        count = 0
        
        for jewel in jewels:
            count += js_dict[jewel]
        
        return count
