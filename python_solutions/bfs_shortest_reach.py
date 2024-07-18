#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

"""
Breadth First Search: Shortest Reach
Problem: https://www.hackerrank.com/challenges/bfsshortreach/problem
Braden Zingler
07/18/2024
"""


def bfs(n, m, edges, s):
    """
    Performs BFS to compute the distances to each node.
    """
    distances = [-1] * n  
    distances[s-1] = 0 

    graph = {i: [] for i in range(1, n+1)}  
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])  # for undirected graph

    queue = deque([s])  # store nodes to visit
    visited = set([s])  # store visited nodes

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor-1] = distances[current-1] + 6

    return [distances[i] for i in range(n) if i != s-1]


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        print(result)