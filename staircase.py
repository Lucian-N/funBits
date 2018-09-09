'''
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to n=4, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size .
'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    block = "#"
    for i in range(n):
        space = " " * (n - i - 1)
        print ( space + block * (i + 1))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
