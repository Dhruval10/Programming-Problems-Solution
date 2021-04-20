class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        answer= []
        count = 0
        temp_string = ''
        for i in range(len(S)):
            if S[i] == '(':
                if count == 0:
                    count += 1
                else:
                    temp_string += S[i]
                    count += 1
            elif S[i] == ')':
                if count == 1:
                    answer.append(temp_string)
                    temp_string = ''
                    count = 0
                else:
                    count -= 1
                    temp_string += S[i]
            # print(temp_string)
        if len(temp_string) > 1:
            answer.append(temp_string)
        
        # print(answer)
        return ''.join(answer)
