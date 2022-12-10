#!/bin/python3

import math
import os
import random
import re
import sys


def hackerrankInString(s):
    # Write your code here
    st = 'hackerrank'
    j = 0
    x = ''
    for i in st:
        while j < len(s):
            if i == s[j]:
                x += str(i)
                j += 1
                break
            else :
                j += 1
    if x == 'hackerrank':
        return 'YES'
    else :
        return "NO"

if __name__ == '__main__':


    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = print(hackerrankInString(s))


