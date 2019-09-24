#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    if len(arr) == 0:
        return # need to return something else here?

    xLen = len(arr)
    yLen = len(arr[0])

    if xLen < 3 or yLen < 3:
        return # need to return something else here? 

    # topLeft = arr[0][0]
    # top = arr[1][0]
    # topRight = arr[2][0]
    # mid = arr[1][1]
    # botLeft = arr[0][2]
    # bot = arr[1][2]
    # botRight = arr[2][2]

    # print(arr[3][2]) #(down, right)
    # print(arr[4][3])
    # print(arr[5][2])
    # sums = []
    maxVal = -float('inf')

    for i in range(0, xLen-2):
        for j in range(0, yLen-2):
            topLeft = arr[i][j]
            top = arr[i][j+1]
            topRight = arr[i][j+2]
            mid = arr[i+1][j+1]
            botLeft = arr[i+2][j]
            bot = arr[i+2][j+1]
            botRight = arr[i+2][j+2]
            val = topLeft+top+topRight+mid+botLeft+bot+botRight
            # sums.append(val)
            maxVal = max(maxVal, val)

    # print(sums)
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
