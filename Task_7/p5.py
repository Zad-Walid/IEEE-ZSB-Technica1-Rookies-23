#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def calc(n):
    d = len(str(n))
    square = str(n ** 2)
    p = len(square)
    if p == 1:
        l = square[0]
        r = square[0]
    else:
        l = square[:p - d]
        r = square[p - d:]

    return int(l) + int(r) == n


def kaprekarNumbers(p, q):
    ans = []
    if p == 1:
        ans.append(1)
    for i in range(p, q + 1):
        if calc(i):
            ans.append(i)
    if len(ans) > 0:
        print(*sorted(ans))
    else:
        print("INVALID RANGE")
    # Write your code here


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)