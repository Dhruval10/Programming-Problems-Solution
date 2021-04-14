from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        items.sort(key=lambda x: x[1], reverse = True)
        answer = defaultdict(list)
        
        for i in range(len(items)):
            answer[items[i][0]].append(items[i][1])
        
        final_answer = []
        
        for key, val in answer.items():
            count = 0
            total = 0
            for j in range(5):
                total += val[j]
                count += 1
            total = total // 5
            final_answer.append([key, total])
        final_answer.sort(key=lambda x: x[0])
        return final_answer
