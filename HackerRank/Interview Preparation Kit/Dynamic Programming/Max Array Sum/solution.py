#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    maxOverall = 0
    ans = []
    ans.append(arr[0])
    maxOverall = max(arr[0], arr[1])
    ans.append(maxOverall)
    i = 2
    for val in arr[2:]:
        opt = max(maxOverall, val + ans[i-2], val)
        # print(ans)
        # print(i-2)
        # print(maxOverall)
        # print(val + ans[i-2])
        # print(val)
        # print("")
        maxOverall = opt
        ans.append(opt) 
        i += 1
    # print(ans)
    return maxOverall

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
