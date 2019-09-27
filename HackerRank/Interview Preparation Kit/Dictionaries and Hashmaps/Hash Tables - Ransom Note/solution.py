#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    check = {}
    for word in magazine:
        if word in check:
            check[word] += 1
        else:
            check[word] = 1
    for word in note:
        if word in check:
            check[word] -= 1
        else:
            check[word] = "Bad"

    for word in check:
        if check[word] == "Bad" or check[word] < 0:
            print("No")
            return

    print("Yes")
    # If negative, bad
    # If new, bad
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)