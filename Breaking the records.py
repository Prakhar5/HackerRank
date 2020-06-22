#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    c=0
    d=0
    m=scores[0]
    n=scores[0]
    for i in range(len(scores)):
        if(scores[i]>m):
            m = scores[i]
            c+=1
        if(scores[i]<n):
            n = scores[i]
            d+=1
    return c,d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
