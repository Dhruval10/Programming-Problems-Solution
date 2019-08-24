import sys 

num = int(input()) 

for i in range(0,num): 
    x = list(input().split()) 
    print(int(x[0]) % int(x[1])) 
