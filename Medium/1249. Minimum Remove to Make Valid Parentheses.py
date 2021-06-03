class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        forward_str = []
        open = 0
        for char in s:
            if char == '(':
                open += 1
            elif char == ')':
                if open == 0:
                    continue
                open -= 1
            forward_str.append(char)
        answer = ''
        for i in range(len(forward_str)-1,-1,-1):
            if open > 0 and forward_str[i] == '(':
                open -= 1
                continue
            answer += forward_str[i]
        
        answer = answer[::-1]
        return answer
