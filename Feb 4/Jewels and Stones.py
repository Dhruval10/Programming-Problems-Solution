class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # create dictionary to count the occurance of each jewel in stones
        jewels_map = defaultdict(int)
        
        # Count occurance
        for str1 in stones:
            jewels_map[str1] += 1
        
        count = 0
        
        # Add the occurance of a jewel in a dictionary
        for str1 in jewels:
            if str1 in jewels_map:
                count += jewels_map[str1]
        
        return count
