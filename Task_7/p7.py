import math
import os
import random
import re
import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    x1=int(y1-y2>0)*10000
    x2=int(m1-m2>0)*(m1-m2)*500
    x3=int(d1-d2>0)*(d1-d2)*15
    if y1!=y2:
     return x1
    elif m1!=m2 :
     return x2
    else :
     return x3

if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = print(libraryFine(d1, m1, y1, d2, m2, y2))

