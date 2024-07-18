#!/bin/python3

import math
import os
import random
import re
import sys

"""
Pairs
Problem: https://www.hackerrank.com/challenges/pairs/problem
Braden Zingler
07/17/2024
"""


def pairs(k, arr):
    """
    Determines the number of pairs of array elements that have a difference equal to the target value.
    k       : the target value
    arr     : the array of elements
    """
    arr.sort()  # sorting array gets all instances of differences of k into close spots within the array
    count = 0
    i, j = 0, 1 # pointers to find locations of differences k

    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            count += 1
            j += 1
        elif diff < k:
            j += 1  # need to increase difference
        else:
            i += 1  # need to decrease difference
    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
