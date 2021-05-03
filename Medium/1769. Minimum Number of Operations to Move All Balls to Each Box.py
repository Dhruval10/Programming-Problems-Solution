class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        answer = [0]*len(boxes)
        
        leftCount, leftWeight, rightCount, rightWeight, n = 0,0,0,0,len(boxes)
        
        for i in range(1,n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftWeight += leftCount
            answer[i] = leftWeight
        
        for i in range(n-2,-1,-1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightWeight += rightCount
            answer[i] += rightWeight

        return answer
