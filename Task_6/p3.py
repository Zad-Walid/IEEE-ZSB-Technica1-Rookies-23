

import math
import os
import random
import re
import sys



def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(list(set(ranked)))
    index = 0
    rank_list = []
    n = len(ranked)
    for i in player:
        while (n > index and i >= ranked[index]):
            index += 1
        rank_list.append(n+1-index)
    return rank_list
if __name__ == '__main__':


    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = print(climbingLeaderboard(ranked, player))




