#!/bin/python3

import math
import os
import random
import re
import sys



def acmTeam(topic):
  list_x = []
  for i in range(len(topic)):
    for j in range(i, len(topic)):
      x = str(int(topic[i])+int(topic[j]))
      list_x.append(x.count("1")+x.count("2"))
  maxi = max(list_x)
  return [maxi,list_x.count(maxi)]


if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = print(acmTeam(topic))


