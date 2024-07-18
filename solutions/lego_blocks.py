#!/bin/python3

import math
import os
import random
import re
import sys

"""
Lego Blocks
Problem: https://www.hackerrank.com/challenges/lego-blocks/problem
Braden Zingler
07/18/2024
"""


def legoBlocks(n, m):
    """
    Compute the total permutations of wall configurations
    int m: the width of the wall
    int n: the height of the wall
    """
    row_combos = [1, 1, 2, 4]   # these are all the base cases
    
    # total combinations for width
    while len(row_combos) <= m:
        row_combos.append(sum(row_combos[-4:]) % (10**9 + 7))

    # extend width to entire height
    total = []
    for col in row_combos:
        total.append(pow(col, n, (10**9 + 7)))

    # find the unstable configs
    unstable = [0, 0]
    for i in range(2, m + 1):
        f = lambda j: (total[j] - unstable[j]) * total[i-j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % (10**9 + 7))

    return (total[m] - unstable[m]) % (10**9 + 7)


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        print(result)