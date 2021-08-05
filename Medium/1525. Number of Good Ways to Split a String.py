from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        
        if len(s) == 1:
            return 0
        
        good_split = 0
        
        word_dict = dict(Counter(s))
        left_dict = defaultdict(int)
        
        for char in s:
            left_dict[char] += 1
            word_dict[char] -= 1
            
            if word_dict[char] == 0:
                del word_dict[char]
            
            if len(left_dict) == len(word_dict):
                good_split += 1
        return good_split
