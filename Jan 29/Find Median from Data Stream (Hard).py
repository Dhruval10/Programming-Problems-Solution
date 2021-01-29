from heapq import heappush, heappushpop, heappop

class MedianFinder:
    

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1, self.heap2 = [], []

    def addNum(self, num: int) -> None:
        min_heap, max_heap = self.heap1, self.heap2
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, num))
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    def findMedian(self) -> float:
        min_heap, max_heap = self.heap1, self.heap2
        if len(max_heap) > len(min_heap):
            return float(max_heap[0])
        return (max_heap[0]-min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()