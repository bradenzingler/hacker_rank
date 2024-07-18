#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

"""
Jesse and Cookies
Problem: https://www.hackerrank.com/challenges/jesse-and-cookies/problem
Braden Zingler
07/18/2024
"""

def cookies(k: int, A: list):
    """
    Determines the number of iterations required to combine cookies to increase the sweetness.
    """
    heapq.heapify(A)
    i = 0

    while len(A) > 1 and A[0] < k:
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        new_sweetness = least_sweet + (2 * second_least_sweet)
        heapq.heappush(A, new_sweetness)
        i += 1
    
    return -1 if A[0] < k else i


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    A = list(map(int, input().rstrip().split()))
    result = cookies(k, A)

    print(result)