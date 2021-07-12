class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        length = len(strs)
        if length == 0:
            return ""
        if length == 1:
            return strs[0]
        
        answer = strs[0]

        for i in range(1,length):
            temp_word = strs[i]
            k = 0
            j = 0
            while j < len(temp_word) and k < len(answer):
                if temp_word[j] == answer[k]:
                    j += 1
                    k += 1
                else:
                    break
            answer = answer[:k]
        return answer
