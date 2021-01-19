class Solution:
    def frequencySort(self, s: str) -> str:
        
        ans_str = ''
        
        characters = set(s)
        
        counts = []
        
        for i in characters:
            counts.append([i,s.count(i)])
        
        counts = sorted(counts, key= lambda x: x[1], reverse = True)
        
        for i,j in counts:
            ans_str += i*j
        
        return ans_str