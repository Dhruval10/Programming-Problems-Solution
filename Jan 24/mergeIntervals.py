class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x:x[0])
        
        answer = []
        
        for interval in intervals:
            if len(answer) == 0:
                answer.append(interval)
            else:
                start_answer = answer[-1][0]
                end_answer = answer[-1][1]
                
                if interval[0] <= end_answer:
                    temp = [start_answer, max(end_answer, interval[1])]
                    answer[-1] = temp
                else:
                    answer.append(interval)
        return answer
