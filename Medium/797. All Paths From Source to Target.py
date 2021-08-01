from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        queue = deque()
        queue.append([0])
        while queue:
            popped = queue.popleft()
            if popped[-1] == len(graph)-1:
                answer.append(popped)
            else:
                for node in graph[popped[-1]]:
                    queue.append(popped+[node])
        return answer
