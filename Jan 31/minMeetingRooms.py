class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        answer = []
        
        intervals = sorted(intervals)
        
        for interval in intervals:
            if len(answer) == 0:
                heapq.heappush(answer, interval[1])
            else:
                if answer[0] <= interval[0]:
                    heapq.heappop(answer)
                heapq.heappush(answer, interval[1])
        return len(answer)