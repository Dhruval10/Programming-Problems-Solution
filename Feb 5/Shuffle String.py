class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        zipped = list(zip(s,indices))
        
        zipped = sorted(zipped, key = lambda x: x[1])
        
        answer_string = ''
        
        for key,value in zipped:
            answer_string += key
        
        return answer_string