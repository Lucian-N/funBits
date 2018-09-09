'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.

 Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
'''


#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_hours = int(s[:2])
    time_minutes = int(s[3:5])
    time_seconds = int(s[6:8])
    
    if s[8] == 'P' and s[:2] !='12':
        time_hours += 12 
    elif s[8] == 'A' and s[:2] == '12':
        time_hours -= 12
    else:
        return s[:8]
    result = str(time_hours).zfill(2) +':' + str(time_minutes).zfill(2)+ ':' + str(time_seconds).zfill(2)
    return result
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
