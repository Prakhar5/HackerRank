#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    n=3
    c=0
    ar=[]
    out = [(s[i:i+n]) for i in range(0, len(s), n)] 
    for i in out:
            if(i[0]!="S"):
                c+=1
            if(i[1]!="O"):
                c+=1
            if(i[2]!="S"):
                c+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
