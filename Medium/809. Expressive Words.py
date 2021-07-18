from collections import Counter
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count_freq(string):
            string_counter = []
            for i in range(len(string)):
                if len(string_counter) == 0 or string_counter[-1][0] != string[i]:
                    string_counter.append([string[i],1])
                else:
                    string_counter[-1][1] += 1
            return string_counter
        if len(s) == 0:
            return 0
        s_freq = count_freq(s)
        count = 0
        for word in words:
            if len(word) == 0 or len(s) < len(word):
                continue
            word_freq = count_freq(word)
            start_s = 0
            start_w = 0
            flag = True
            if len(word_freq) != len(s_freq):
                continue
            while start_s < len(s) and start_w < len(word_freq):
                # print(word_freq[start_w][0], s_freq[start_s][0])
                if (word_freq[start_w][0] == s_freq[start_s][0] and word_freq[start_w][1] == s_freq[start_s][1]):
                    start_s += 1
                    start_w += 1
                elif s_freq[start_s][1] >= 3 and word_freq[start_w][0] == s_freq[start_s][0] and word_freq[start_w][1] <= s_freq[start_s][1]:
                    start_s += 1
                    start_w += 1
                else:
                    flag = False
                    break
            if flag == True:
                # print(word)
                count += 1
        return count
