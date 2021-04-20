class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        answer = []
        
        array = [i for i in range(1,target[-1]+1)]
        
        j = 0
        
        for i in range(len(array)):
            if array[i] == target[j]:
                answer.append("Push")
                j+=1
            else:
                answer.append("Push")
                answer.append("Pop")
        return answer
