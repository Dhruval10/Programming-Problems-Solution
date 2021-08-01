class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        count = 0
        lefts = 0
        leftt = 0
        
        while leftt < len(target):
            temp_str = ''
            lefts = 0
            while lefts < len(source) and leftt < len(target):
                if source[lefts] == target[leftt]:
                    temp_str += source[lefts]
                    lefts += 1
                    leftt += 1
                else:
                    lefts += 1
            if len(temp_str) == 0:
                return -1
            count += 1
        return count
