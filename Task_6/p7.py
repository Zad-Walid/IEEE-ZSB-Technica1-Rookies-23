import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    # Write your code here
    z=0
    for i in arr:
        for j in arr:
            if(j-i==d):
                if((j+d) in arr):
                    z+=1
    return z

if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = print(beautifulTriplets(d, arr))


