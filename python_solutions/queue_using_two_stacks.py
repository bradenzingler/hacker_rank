#!/usr/bin/python3

"""
Queue using Two Stacks
Problem: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
Braden Zingler
07/17/2024
"""

class Queue:
    
    def __init__(self):
        """
        Initializes a new queue with two empty stacks.
        """
        self.stack_1 = []
        self.stack_2 = []
    

    def enqueue(self, val):
        """
        Adds a new element to the end of the queue.
        """
        self.stack_1.append(val)


    def dequeue(self):
        """
        Removes the element from the front of the queue and returns it.
        """
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


    def head(self):
        """
        Print the element at the front of the queue.
        """
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2[-1]
    

if __name__ == '__main__':

    num_queries = int(input()) 
    queue = Queue()

    for query_itr in range(num_queries):
        curr_cmd = input()
        
        # Enqueue command: 1 val
        if curr_cmd[0] == "1":
            query_val = int(curr_cmd.split(" ")[1])
            queue.enqueue(query_val)

        # Dequeue command: 2
        elif curr_cmd[0] == "2":
            queue.dequeue()

        # Head command: 3
        elif curr_cmd[0] == "3":
            print(queue.head())