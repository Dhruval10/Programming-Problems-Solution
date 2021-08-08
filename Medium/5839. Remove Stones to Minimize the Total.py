import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heaps = []
        total = 0
        for i in range(len(piles)):
            heapq.heappush(heaps,-piles[i])
            total += piles[i]
        while k > 0:
            k -= 1
            temp1 = -heapq.heappop(heaps)
            # total -= temp1
            total -= (temp1)//2
            heapq.heappush(heaps,-(temp1-(temp1)//2))
        return total
