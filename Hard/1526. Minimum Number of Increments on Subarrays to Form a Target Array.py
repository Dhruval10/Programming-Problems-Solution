class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        steps = [0 for _ in range(len(target))]
        
        past_min = 0
        
        for i in range(len(target)):
            if target[i] > past_min:
                steps[i] = target[i]-past_min
            past_min = target[i]
            
        return sum(steps)
