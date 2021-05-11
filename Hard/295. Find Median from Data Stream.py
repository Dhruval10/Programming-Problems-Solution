class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        # heapq.heappush(self.minHeap, -num)
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, -num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap,num))

    def findMedian(self) -> float:
        # print(self.minHeap, self.maxHeap)
        if len(self.minHeap) == len(self.maxHeap):    
            return (-self.minHeap[0] + self.maxHeap[0]) / 2.0
        else:
            return self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
