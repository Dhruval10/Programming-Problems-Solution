from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        paths_dict = defaultdict(int)
        words.sort(key=lambda x:len(x))
        max_chain = 1
        for word in words:
            paths_dict[word] = 1
            for j in range(len(word)):
                temp_word = word[:j]+word[j+1:]  # Delete current character and see if the updated word is present in our hashmap or not
                if temp_word in paths_dict:
                    paths_dict[word] = max(paths_dict[temp_word]+1,paths_dict[word])
                    max_chain = max(max_chain,paths_dict[word])
        return max_chain
