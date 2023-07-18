#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  # creating the answer
  ans = ''

  #making sure the first character is uppercased
  ans = ans + s[0].upper()

  #looping through chars of input string
  for i in range(1, len(s)):
    #if before we had a space and the current
    # is an alphanumeric value we send it to uppercase
    if s[i-1] == ' ' and s[i].isalpha():
      ans = ans + s[i].upper()
    #copying the rest of the string
    else:
      ans = ans + s[i]
      
  return ans

if __name__ == '__main__':
    #HackerRank system
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()

    result = solve(s)

    print(result)
    #HackerRank system
    #fptr.write(result + '\n')