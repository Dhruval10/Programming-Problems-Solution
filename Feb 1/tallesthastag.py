# import math

def tallesthastag(position,heights): 
    maxheight=0
    for i in range(1,len(position)): # note that the length of positions start at 1
        if abs(position[i-1]-position[i])>1: # that positions are not adjacent 
            maxheight=max(maxheight,getMaxHeight(position[i-1],position[i],heights[i-1],heights[i]))
    return maxheight

def getMaxHeight(p1,p2,h1,h2): 
    shorter=min(h1,h2)
    taller=max(h1,h2)
    gap=abs(p1-p2)-1
    if taller>shorter+gap: 
        return shorter+gap 
    else: 
        diff=taller-shorter
        gap=gap-diff
        return int(taller+gap/2) if gap%2==0 else int(taller+gap//2+1)

print(tallesthastag([1,2,4,7],[4,5,7,11]))
print(tallesthastag([2,1,10],[2,1,5]))
print(tallesthastag([3,1,3,7],[3,4,3,3]))