'''
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
'''


#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
            
    comparison = [a_score, b_score]
    return comparison

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')