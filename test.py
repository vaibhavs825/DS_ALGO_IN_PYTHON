#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumPouringWaterPenalty function below.
from collections import defaultdict

def createGraph(parent,g):
    for i in range(1,len(parent)):
        g[parent[i]].append(i)

def dfs(src,waterlevel,cost,apple,val,g):
    if not g.get(src,None):
        if waterlevel[src]==apple:
            val[src]=cost
            return cost
        return 0

    if g.get(src,None):
        penalty = 0
        if waterlevel[src]==apple:
            penalty = cost
        for t in g[src]:
            penalty += dfs(t,waterlevel,cost,apple,val,g)
    val[src] = penalty
    return penalty


def minimumPouringWaterPenalty(parent, waterLevel, overhydratedPenalty, underhydratedPenalty):
    g = defaultdict(list)
    h_penalty = [0]*len(waterLevel)
    u_penalty = [0]*len(waterLevel)
    createGraph(parent,g)
    dfs(0,waterLevel,overhydratedPenalty,1,h_penalty,g)
    dfs(0,waterLevel,underhydratedPenalty,-1,u_penalty,g)
    ans = float("inf")
    p = u_penalty[0]
    for i,h in enumerate(h_penalty):
        ans = min(ans,h+(p-u_penalty[i]))
    return ans


if __name__ == '__main__':

    minimumPouringWaterPenalty([-1, 0, 1], [1, 1, 1], 3, 5)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # parent_count = int(input().strip())
    #
    # parent = []
    #
    # for _ in range(parent_count):
    #     parent_item = int(input().strip())
    #     parent.append(parent_item)
    #
    # waterLevel_count = int(input().strip())
    #
    # waterLevel = []
    #
    # for _ in range(waterLevel_count):
    #     waterLevel_item = int(input().strip())
    #     waterLevel.append(waterLevel_item)
    #
    # overhydratedPenalty = int(input().strip())
    #
    # underhydratedPenalty = int(input().strip())
    #
    # res = minimumPouringWaterPenalty(parent, waterLevel, overhydratedPenalty, underhydratedPenalty)
    #
    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
