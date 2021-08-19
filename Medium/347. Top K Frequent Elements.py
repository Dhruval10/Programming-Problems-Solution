class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_count = {}
        
        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
        
        freq_count = sorted(list(freq_count.items()), key=lambda x: -x[1])
        
        answer = []
        
        for i in range(k):
            answer.append(freq_count[i][0])
        
        return answer
