class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        answer = []
        for query in queries:
            count = 0
            for point in points:
                if pow(point[0]-query[0],2) + pow(point[1]-query[1],2) <= pow(query[2],2):
                    count += 1
            answer.append(count)
        return answer
