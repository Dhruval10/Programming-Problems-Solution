class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        arrayList = [intervals[0]]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] <= arrayList[-1][1]:
                arrayList[-1][1] = max(arrayList[-1][1],intervals[i][1])
            else:
                arrayList.append(intervals[i])
        
        return arrayList
