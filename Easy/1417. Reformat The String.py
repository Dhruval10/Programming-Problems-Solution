class Solution:
    def reformat(self, s: str) -> str:
        
        alpha = []
        numeric = []
        
        for i in range(len(s)):
            if s[i].isalpha():
                alpha.append(s[i])
            elif s[i].isnumeric():
                numeric.append(s[i])
        
        if abs(len(alpha) - len(numeric)) > 1:
            return ""
        
        final_answer = ""
        start = 0
        
        if len(alpha) > len(numeric):
            for i in range(len(numeric)):
                final_answer += alpha[i]
                final_answer += numeric[i]
            final_answer += alpha[-1]
        elif len(alpha) < len(numeric):
            for i in range(len(alpha)):
                final_answer += numeric[i]
                final_answer += alpha[i]
            final_answer += numeric[-1]
        else:
            for i in range(len(alpha)):
                final_answer += numeric[i]
                final_answer += alpha[i]
        return final_answer
