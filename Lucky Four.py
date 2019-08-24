import sys 

num = int(input()) 

for i in range(num): 
    count = 0 
    x = (sys.stdin.readline()) 

    for j in range(0,len(x)): 
        if(x[j] is '4'): 
        count = count+1 
    print(count) 
