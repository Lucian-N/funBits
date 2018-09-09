'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    length =len(arr)
    arr = sorted(arr)
    min_sum = 0
    max_sum = 0 
    
    for i in range(length-1):
        min_sum += arr[i]
    for i in range(1, length):
        max_sum += arr[i]

    print (min_sum, end=" ")
    print (max_sum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
