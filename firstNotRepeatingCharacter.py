from collections import defaultdict

def firstNotRepeatingCharacter(s):
    
    dict1 = defaultdict(int)
    
    for i in s:
        dict1[i] += 1
    
    for key, values in dict1.items():
        if values == 1:
            return key
    return '_'
