class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dict1 = collections.defaultdict(int)
        
        mini = math.inf
        
        for i in range(len(wordsDict)):
            dict1[wordsDict[i]] = i
            if word1 == wordsDict[i] or word2 == wordsDict[i]:
                if word1 in dict1 and word2 in dict1:
                    mini = min(mini, abs(dict1[word1] - dict1[word2]))
        return mini
    '''
        Dhruval
    '''
