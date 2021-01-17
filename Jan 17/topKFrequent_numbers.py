class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        
        list = {}
        
        # words = sorted(words)
        
        for i in range(len(words)):
            if words[i] not in list:
                list[words[i]] = 1
            else:
                list[words[i]] += 1
        
        list = sorted(list.items(), key = lambda x: x[1], reverse = True)
        
        ans_list = []
        
        for i in range(k):
            ans_list.append(list[i][0])

        return ans_list
        
#         dict = defaultdict(int)
#         answer = []
        
#         for number in nums:
#             dict[number] += 1
        
#         heap = []
        
#         for key, value in dict.items():
#             heapq.heappush(heap, (-value, key))
        
#         while k > 0:
#             answer.append(heapq.heappop(heap)[1])
#             k -= 1
        
#         return answer
