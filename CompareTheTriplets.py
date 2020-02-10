#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    A = a
    B = b
    score_alce=0;
    score_bob=0;
    for i in range(len(a)):
        if(A[i]>B[i]):
            score_alce+=1
        if(A[i]<B[i]):
            score_bob+=1
        #if(A[i]==B[i]):
            
    return score_alce,score_bob;


if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
