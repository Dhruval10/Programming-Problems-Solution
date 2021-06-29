from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:        
        count_dict = defaultdict(int)
        for i in range(len(cpdomains)):
            freq, url = cpdomains[i].split()
            if url in count_dict:
                count_dict[url] += int(freq)
            else:
                count_dict[url] = int(freq)
            for j in range(len(url)):
                if url[j] == '.':
                    temp_url = url[j+1:]
                    if temp_url in count_dict:
                        count_dict[temp_url] += int(freq)
                    else:
                        count_dict[temp_url] = int(freq)
        answer = []
        for key, val in count_dict.items():
            answer.append(str(val) + " " + key)
        return answer
