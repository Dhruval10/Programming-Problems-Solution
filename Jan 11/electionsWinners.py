def electionsWinners(votes, k):
    m = max(votes)
    c = 0
    if(k==0):
        for v in votes:
            if(v==m):
                c+=1
        if(c==1):
            return 1
        else:
            return 0
    for v in votes:
        if(v+k>m):
            c+=1
    return c