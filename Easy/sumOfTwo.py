def sumOfTwo(a, b, v):
    
    dict_a = {}
    # dict_b = {}
    
    for i in range(len(a)):
        dict_a[v - a[i]] = 1
    
    for value in b:
        if value in dict_a:
            return True
    return False
