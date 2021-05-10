class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Function which checks whether the given word is present in dictionary or not
        def isContain(word, dict1):
            temp_str = ''
            for i in range(len(word)):
                temp_str += word[i]
                if temp_str in dict1:
                    pass
                else:
                    return False
            return True
        
        # dictionary for word searching 
        dict1 = dict()
        for word in words:
            dict1[word] = 1
        # Sort dictionary
        words.sort()
        # Sort dict by word length. (- is for sorting in reverse)
        words.sort(key=lambda x:-len(x))
        
        # Return first word  whose sub-parts are in the dictionary
        for word in words:
            if isContain(word,dict1):
                return word
