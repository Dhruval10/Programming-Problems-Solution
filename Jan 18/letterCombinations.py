class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numbers = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        # answer = ['a']*len(numbers[digits[0]])*len(numbers[digits[1]])
        answer = []
        if len(digits) == 1:
            for i in range(len(numbers[int(digits[0])])):
                answer.append(numbers[int(digits[0])][i])
        
        if len(digits) == 2:
            for i in range(len(numbers[int(digits[0])])):
                for j in range(len(numbers[int(digits[1])])):
                    answer.append(numbers[int(digits[0])][i] + numbers[int(digits[1])][j])
        if len(digits) == 3:
            for i in range(len(numbers[int(digits[0])])):
                for j in range(len(numbers[int(digits[1])])):
                    for k in range(len(numbers[int(digits[2])])):
                        answer.append(numbers[int(digits[0])][i] + numbers[int(digits[1])][j] + numbers[int(digits[2])][k])
        if len(digits) == 4:
            for i in range(len(numbers[int(digits[0])])):
                for j in range(len(numbers[int(digits[1])])):
                    for k in range(len(numbers[int(digits[2])])):
                        for l in range(len(numbers[int(digits[3])])):
                            answer.append(numbers[int(digits[0])][i] + numbers[int(digits[1])][j] + numbers[int(digits[2])][k] + numbers[int(digits[3])][l])
            
            
            
        return answer