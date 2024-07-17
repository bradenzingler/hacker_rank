#!/bin/python3

"""
Balanced Brackets
Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem
Braden Zingler
07/17/2024
"""

import math
import os
import random
import re
import sys


def isBalanced(s):
    """
    Determines if a sequence of brackets is balanced, using a stack to track opening brackets.
    """
    stack = []      # track opening brackets
    char_dict = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    
    for char in s:
        
        # opening bracket
        if char in char_dict:
            stack.append(char)

        # closing bracket
        else:
            if not stack:   # stack empty, but closing bracket
                return "NO"
            
            top = stack.pop()
            if char_dict[top] != char: 
                return "NO"
    
    # if stack isn't empty, there are unmatched closing brackets
    return "NO" if stack else "YES"


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)

