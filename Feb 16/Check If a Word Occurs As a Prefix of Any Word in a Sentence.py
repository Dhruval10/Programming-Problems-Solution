class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        
        def checkString(string1, searchWord):
            string1 = string1.lower()
            searchWord = searchWord.lower()
            
            if len(string1) >= len(searchWord):
                for i in range(len(searchWord)):
                    if searchWord[i] != string1[i]:
                        return False
                return True
            else:
                return False
        
        sentence = sentence.split()
        
        for i in range(len(sentence)):
            if sentence[i][0] == searchWord[0]:
                if checkString(sentence[i], searchWord) == True:
                    return i+1
            else:
                pass
        
        return -1