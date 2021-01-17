class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for point in points:
            heapq.heappush(heap, (sqrt(point[0]**2 + point[1]**2), point))

        answer = []
        while K > 0:
            answer.append(heapq.heappop(heap)[1])
            K -= 1
        return answer
