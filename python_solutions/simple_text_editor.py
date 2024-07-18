#!/bin/python3

import math
import os
import random
import re
import sys

"""
Simple Text Editor
Problem: https://www.hackerrank.com/challenges/simple-text-editor/problem
Braden Zingler
07/17/2024
"""

class TextEditor:

    def __init__(self):
        """
        Initializes the text editor with an initial empty array to store the string characters.
        """
        self.s = []
        self.history = []
    

    def append(self, w):
        """
        Append string W to the end of S.
        """
        self.history.append(self.s.copy())
        for char in w:
            self.s.append(char)
    

    def delete(self, k):
        """
        Delete the last k characters of S.
        """
        self.history.append(self.s.copy())
        if k >= len(self.s):
            self.s = []
        else:
            self.s = self.s[:-k]
    

    def print(self, k):
        """
        Print the kth character of S.
        """
        print(self.s[k])


    def undo(self):
        """
        Undo the last operation of type 1 or 2, 
        reverting S to the state it was in prior to the operation.
        """
        if self.history:
            self.s = self.history.pop()


if __name__ == "__main__":
    q = int(input())

    editor = TextEditor()

    for input_line in range(q):
        command = input()

        # append command
        if command[0] == "1":
            string_input = str(command.split(" ")[1])
            editor.append(string_input)

        # delete 
        elif command[0] == "2":
            k = int(command.split(" ")[1])
            editor.delete(k)

        # print
        elif command[0] == "3":
            k = int(command.split(" ")[1]) - 1
            editor.print(k)

        # undo
        elif command[0] == "4":
            editor.undo()