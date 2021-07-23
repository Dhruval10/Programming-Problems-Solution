from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        dict1 = defaultdict(list)
        
        for x,y in edges:
            dict1[x].append(y)
            dict1[y].append(x)
        
        dict1 = list(dict1.items())
        
        center = 0
        maxi = 0
        
        for i in range(len(dict1)):
            if len(dict1[i][1]) > maxi:
                center = dict1[i][0]
                maxi = len(dict1[i][1])
        return center
