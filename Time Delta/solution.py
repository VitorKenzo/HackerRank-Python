#!/bin/python3

import math
import os
import random
import re
import sys

# importing the datetime object to make our lives easier
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    # transforming the strings in datetime objects
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    
    #getting the answer
    delta = t1 - t2

    #returnin the answer in the correct format
    return str(abs(int(delta.total_seconds())))

# the main was given in the exercise and I changed it so that the
# out was just a print in the screen
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)

        #fptr.write(delta + '\n')

    #fptr.close()