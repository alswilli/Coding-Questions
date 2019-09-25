#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # Brute Force -> O(n^2)
    # Other method - Hash Table (check for sum of zeroes)
    hashTable = {}
    counter = 0

    for char in a:
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    for char in b:
        if char in hashTable and hashTable[char] > 0:
            hashTable[char] -= 1
        else:
            counter += 1

    for key in hashTable:
        if hashTable[key] != 0:
            counter += hashTable[key]

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
