'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left_difference = 0 
    right_difference = 0
    
    for i in range(n):
        left_difference += arr[i][i]
        right_difference += arr[i][n-i-1] 
        
    if left_difference < right_difference:
        return right_difference - left_difference
    else:
        return left_difference - right_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
