class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dict1 = collections.defaultdict(int)
        
        for i in range(len(arr)):
            dict1[arr[i]] += 1
        
        values = dict(collections.Counter(list(dict1.values())))
        
        for key, value in values.items():
            if value != 1:
                return False
        return True
