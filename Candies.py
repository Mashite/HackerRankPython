# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:27:41 2021

@author: masit
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    n=len(arr)
    arrLeft=[1]*n
    arrRight=[1]*n
    sum=0;
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            arrLeft[i]=arrLeft[i-1]+1
        else:
            arrLeft[i]=1
            
    for j in range (n-2,-1,-1):
        if arr[j]>arr[j+1]:
            arrRight[j]=arrRight[j+1]+1
        else:
            arrRight[j]=1
            
    for i in range(0,n):
        sum= sum+ max(arrLeft[i],arrRight[i])
    return sum;

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)
    
    print(str(result) + '\n')

   # fptr.write(str(result) + '\n')

   #fptr.close()
